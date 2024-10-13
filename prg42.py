#словари
# d = dict() - пустой словарь
# d = {} - пустой словарь
from prg39 import value

d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple',
    'меню': ['суп','тефтели','чай']
}
print (d['стол'][0])
d ['слива'] = 'plum'
d[0] = 'one'
d[36.6] = 'normal'
d['True'] = 'Истина'
print(len(d))
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
if 'Истина ' in d.values():
    print('Истина есть среди значений')
for keys in d. keys():
    print(f'ключ:{key}, занчение:{d[key]}')
for keys,value in d.items():
    if value == 'Истина':
    print(f'Для Истина ключ - {key}')
print(d.get('груша'))
del d['стул']
print(d)