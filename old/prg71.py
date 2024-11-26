# Syntax sugar( синтаксический сахар)
#печать = print

#печать('Здравстрвуйте', 'До свидания', sep=' и ')

a = list(range(1,11))

#функция высшего порядка map
b = list(map(str, a))
print(b)
res = ' и '.join(b)

print(res)
# список квадратов чисел из исходного списка
def square(num):
    return num **2
# square , поскольку простая, может быть записана и так
#ll = lambda num: num **2

sq = list(map(lambda num: num **2,a))

print(sq)

fruits = ['арбуз', 'ананас', 'банан', 'яблоко', 'манго']
fruits.sort(key=lambda letter:letter[2])
print(fruits)