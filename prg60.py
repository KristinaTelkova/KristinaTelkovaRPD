
length = 3
try:
    text = input('Введите любой текст: ')
    assert len(text) > length
    print(f'Вы ввели : {text}')
except AssertionError:
    print(f'Нет , ваш текст короче ,чем {length} символа')