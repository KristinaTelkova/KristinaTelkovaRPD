text= 'о сколько нам открытий чудных! открытий , закрытий'

temp = '!,.;?:'
p = list(temp)
for item in p:
    text = text.replace(item,'')
lst= text.split()
print(lst)
word = ' P y  th on'

word = ''.join(word.split())
print(word)