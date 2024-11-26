#Create Read(Retrieve) Update Delete
#CRUD
#PEP 249 (connection, cursor)
import sqlite3

#Подключение (connection)
connection = sqlite3.connect('films_db.sqlite')

#Создаём курсор
cursor=connection.cursor()

#исполнение запроса
result = cursor.execute("""
    UPDATE films
    SET duration = 282
    WHERE title = 'Аватар'
""")
#подтвержаем все изменения в БД
choice = input('Вы действительно хотите удалить(Y/N):')
if choice =='Y':
    connection.commit()

elements=result.fetchall()

for item in elements:
    print(item)

#закрытие соединения с базой
connection.close()