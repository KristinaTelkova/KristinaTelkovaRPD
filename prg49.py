#чтение нескольких стрко
fo = open('sample.txt', 'rt', encoding = 'UTF-8') # по умолчанию режим wt
#print(dir(fo))
text = fo.readline()
while text != '':
    print(text , end = '')
    text = fo.readline()
fo.close()
