# Файлы (запись)
#Бывают текстовые и бинарные (двоичные)
# Режимы: r -read; w- write, a -append
# Подрежим: b -binary , t - text
fo = open('sample.txt', 'rt', encoding = 'UTF-8') # по умолчанию режим rt
print(fo.name,fo.mode, fo.encoding)
fo.read(10)
text = fo.read(6)
print(text)
fo.close()