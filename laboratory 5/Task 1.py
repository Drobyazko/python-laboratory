n = 0
while n!=1:
    print("Enter list")
    list=input().split(' ')
    result = []
    for element in list:
        for part in element:
            result.append(part)
    print(result)
    print("Enter 0 if you want to continue and 1 if you want to stop")
    n = int(input())

n = 0
while n!=1:
    print("Enter list")
    listik = input().split(' ')
    result = list("".join(listik))
    print (result)
    print("Enter 0 if you want to continue and 1 if you want to stop")
    n = int(input())


from functools import reduce
def reducer(el_prev, el):
    return el_prev + el
listik = input("Введіть список: ").split(' ')
a = reduce(reducer, listik)
print(list(a))
