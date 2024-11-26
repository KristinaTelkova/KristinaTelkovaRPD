#операции между кортежами и другими объектами
s ='Python'
s = (255,128,64)
lst = ['бремя','время','стремя']
#temp = list(enumerate(lst))
#print(temp)
#print(sorted(s))
for index, value in enumerate(lst):
    print(f'Для данного списка:\n индекс-{index}\n значение- {value}')

for index, value in enumerate(lst):
    print(f'{index+1}. {value}')