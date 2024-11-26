# Файлы (запись)
#Бывают текстовые и бинарные (двоичные)
# Режимы: r -read; w- write, a -append
# Подрежим: b -binary , t - text

total = 0
fo = open('../sample.txt', 'at', encoding ='UTF-8') # по умолчанию режим rt
fo.write('\n')
num = fo.write('Это первая строка внутри файла\n')
total += num
num = fo.write('Это вторая строка внутри файла\n')
total += num
print(f'В файле записано {total} байт')
fo.close()