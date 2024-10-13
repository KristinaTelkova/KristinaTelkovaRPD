import string as s
import random as r
num = 12
# Делаем набор букв и цифр
set_of_sympols = s.digits+s.ascii_lowercase+ s.ascii_uppercase
# Делаем множество
set_of_sympols = set(set_of_sympols)
# удаляем сомнительные символы
set_of_sympols = set_of_sympols - {'0','O','1','I','l'}
# делает строку
set_of_sympols = list(set_of_sympols)
# перемешиваем

# делаем нужное колличество символов
temp = set_of_sympols[:num]
temp += ['@','&','$','?']
r.shuffle(temp)
# делаем ствоку без пробелов
password = ''.join(temp)
print(password)