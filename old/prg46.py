# Файлы (запись)
#Бывают текстовые и бинарные (двоичные)
# Режимы: r -read; w- write, a -append
# Подрежим: b -binary , t - text
fo = open('../sample.txt', 'wt', encoding ='UTF-8') # по умолчанию режим wt
print(fo.name,fo.mode, fo.encoding)
num = fo.write('Это текст внутри файла')
print(num)
fo.close()