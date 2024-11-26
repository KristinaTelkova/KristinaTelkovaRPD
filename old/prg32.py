#Списки
from array import array

array = []
array = list()
# index 0 1
array = ['ясно', 'пасмурно']
print(array)
print(array[1]) #выводит 1 элемент array
print(array[1][1]) #выводит букву (1 элемент слова)
okroshka = ['кефир','квас','огурец','перец', 'соль']
print(okroshka[1:3])
print(okroshka[::2]) #вывыдоим через одно слово

word = ('pithon')
#word[1] = 'y' - так нельзя
lst = list(word)
print(lst)
lst[1] = 'y'
print(*lst, sep='')
dishes = ['суп', 'пюре', 'компот']
first, second, third = dishes
print(second)
*eat, drink = dishes
print(eat)