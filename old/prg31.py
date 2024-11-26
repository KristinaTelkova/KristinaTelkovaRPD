#Функции-антонимы chr и ord
import string as s
temp = s.digits + s.ascii_lowercase + s.ascii_uppercase
m_set = set(temp) - {'l','O','I','T'} #удаляет симовлы в множестве

print(set(temp))
print(ord('а'))
print(chr(97))
s = '"Привет"'
print(ord('"'))
print(f'{chr(171)}Привет{chr(187)}')
print(chr(10000))

#x\ = chr (176) - одно и тоже

print('\u4574') #Unicode
print('75\xBO') # hex на калькуляторе ASCII