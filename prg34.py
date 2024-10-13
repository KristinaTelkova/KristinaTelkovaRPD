#от строк к спискам
from prg25 import result

a = ['кефир', 'квас', 'огурец', 'перец', 'соль', 'колбаса',
 'редис', 'картошка', 'укроп', 'петрушка']
b = a[:3]
b.sort()
#вывод список строкой
print(*b, sep=',') # 1 способ
result = ','.join(b) # 2 способ
print(result)

word = 'pithon'
lst = list(word)
lst[1]= 'y'
result = ''.join(lst)
print(result)