#Модули


def summ(a,b):
    try:
        res = a+b
    except TypeError:
        return ('Складываю только числа')
    else:
        return res

first = 8
second = 4


def sub(a,b):
    try:
        res = a-b
    except TypeError:
        return ('Вычитаю только числа')
    else:
        return res

def divide(a,b):
    try:
        res = a/b
    except TypeError:
        return ('Вычитаю только числа')
    except ZeroDivisionError:
        return ('На ноль делить нельзя')
    else:
        return res

def multi(a,b):
    try:
        res = a*b
    except TypeError:
        return ('Вычитаю только числа')
    except ZeroDivisionError:
        return ('На ноль делить нельзя')
    else:
        return res

first = 8
second = 4
print(summ(first,second))
print(sub(first,second))
print(divide(first,second))
print(multi(first,second))