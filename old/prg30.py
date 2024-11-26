# Форматирование строк
# %s -для подстановки str
# %d -для подстановки int
# %f -для подстановки float
name = 'Виктор'
age = 9
height = 141.5

#f_string ='%18s,\nвозраст: %2d,\nрост: %6.1f см' % \
        #  (name, age, height)
#print(f_string) #метод плейсхолдеров

#использование метода формат (именованные аргументы)
#f_string = 'Имя: {N}, возраст: {A} лет, рост: {H}'.format(N=name, A=age, H=height)
#print(f_string)

#позиционные элементы
#f_string = 'Имя: {:s}, возраст: {:d} лет, рост: {:.2f}'\
 #   .format(name, age, height)

#print(f_string)
#Интерполяция строк
f_string = f'Имя:{name}, возраст:{age}, рост:{height:.2f}'
print(f_string)
f_string += f'При фигуре из 4 сторон угол будет {360 / 4}'