#Умножение списка на число =повторяющиеся значения в списке
#a = [0,1] *5
# a=[[1,2,3],[4,5,6],[7,8,9]]
a=[[x for x in range(i,13,4)] for i in range(1,5)]
print(a)