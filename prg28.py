s = input('Введите строку: ')

temp = s[::-1]
if temp == s:
    print('да')
else:
    print('нет')