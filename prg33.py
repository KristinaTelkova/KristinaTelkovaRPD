# операции со списками и методы
okroshka = ['кефир','квас','огурец','перец', 'соль']
additional = ['колбаса','редис','картошка']
final = okroshka + additional
final += ['укроп']
print(final+['петрушка'])
print('Ингридиентов в окрошке:',len(final))
final.sort() # сортирует по алфавиту
#способ 1
#count = 1
#for item in final:
#    print(f'\t{count}. {item}')
#    count +=1
count = 1
for item in range(len(final)):
    print(f'\t{item+1}. {final[item]}')

print('\t',*final , sep='\n\t')

print(final.index('перец'))
temp= final.pop(2)
print(temp)
final.remove('соль')
final.insert(4,temp)