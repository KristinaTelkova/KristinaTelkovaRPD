s = 'Язык Python'

print(s.lower()) # все буквы маленькие

print(s.upper()) #все буквы большие
print(s.capitalize()) # Первое слово с большой буквы, остальные с маленькой
print(s.title()) #все слова с большой буквы
print(s.strip()) # убирает указанные символы слева и справа, можно использовать,
#чтобы убирать пробелы
print(s.lstrip()) # убирает указанные символы слева
print(s.rstrip()) # убирает указанные символы справа
 # res = input('Введите строку:').lower() #пример введения строки и применение lower
 # res = input('Введите строку:').lower().strip() - цепочка последовательности, выполняется
 #по порядку
print(s.count('Я')) #считает колличество повторяющихся элементов
print(s.count('e', 4 ,6)) #Считает от 4 до 6 элемента
print(s.index('з')) #индекс по символу или строке
print(s.find('ы', 2, 5)) # ищет индекс вхождения со втрого по 5 элемент
print(s.replace('ы','е', 1)) # замена элементов стоки с указанием кол-ва
print(s.startswith('Яз')) # проверяет , начинается ли строка на заданный элемент
if (s.startswith('Я')):# if s[0:4] == 'Я'
    pass
