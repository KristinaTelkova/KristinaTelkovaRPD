#метода списков и строк
text= 'о сколько нам открытий чудных о сколько нам открытий чудных'
# lst= list(text) - разбивает по буквам , не подходит
lst = text.split() #любое колличество пробелов всегда будет одним
lst = set(lst) #превращаем в множество
lst= list(lst) #превращаем в список
lst.sort() #отсортировали
for word in lst:
    if len(word) > 2:
        print(word)
lst= text.split ()
count = lst.count ('сколько')
print(f'Слово "сколько" посторилось {count} раз')