from functools import reduce
def reducer(el_prev, el):
    return el_prev + el
listik = input("Введіть строку: ").split(' ')
a = reduce(reducer, listik)
print(list(a))