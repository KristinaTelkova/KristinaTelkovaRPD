import configparser
import datetime
import os
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm
from forms.add_news import NewsForm



from flask import Flask, url_for, request, render_template, abort
from flask import flash, redirect, make_response, session
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_login import current_user


from forms.loginform import LoginForm



current_directory = os.path.dirname(__file__)
UPLOAD_FOLDER = f'{current_directory}/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)  # привязали менеджер авторизации к приложению

app.config['SECRET_KEY'] = 'too_short_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

config = configparser.ConfigParser()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def user_loader(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['text'] = 'Этот текст отобразится на главной странице'
    param['title'] = 'Главная'
    return render_template('index.html', **param)

@login_manager.user_loader
def user_loader(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    # session.pop('visit_count', None) # если надо программно уничтожить сессию
    return make_response(f'Вы посетили данную страницу {visit_count} раз.')


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(f'Вы посетили данную страницу {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response('За последние два года вы посетили данную страницу впервые.')
        res.set_cookie('visit_count', '1', max_age=60 * 60 * 24 * 365 * 2)
        # res.set_cookie('visit_count', '1', max_age=0) # удаляем cookies
    return res


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')  # request.url, либо на нужную страницу
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form, message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form, message=f'Пользователь с E-mail {form.email.data} уже есть')
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Ошибка авторизации',
                               message='Неправильная пара: логин - пароль!',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# добавление новости
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/blog')
    return render_template('add_news.html', title='Добавление отзыва',
                           form=form)


# редактирование новости
@app.route('/blog/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
            form.submit.label.text = 'Отредактировать'  # заменяем надпись на кнопке
        else:
            abort(404)

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/blog')
        else:
            abort(404)
    return render_template('add_news.html', title='Редактирование отзыва',
                           form=form)


# удаление новости
@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/blog')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
        param = {}
        param['text'] = 'Этот текст отобразится на главной странице'
        param['title'] = 'Главная'
        return render_template('contacts.html', **param)



@app.route('/about')
def about():
    params = {}
    params['title'] = 'О нас'
    params['text'] = 'Мы перспективная и динамично развивающаяся компания...'
    return render_template('about.html', **params)


@app.route('/blog')
def blog():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private == False)
    return render_template('blog.html', title='Новости', news=news)


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    app.run(port=5000, host='127.0.0.1')
