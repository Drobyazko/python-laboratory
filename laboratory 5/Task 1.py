# Перетворити список, у якому елементи представляють групи символів, у список з поодинокими символами, вибраними з цих груп. Необхідно:
#  виконати це завдання 4-ма варіантами, визначити час виконання кожним і знайти самий швидкодіючий;
#  1-ий варіант: працювати з оператором for (це найпростіший варіант);
#  2-ий варіант: застосувати функцію join.
#  3-ий варіант: застосувати функціональне програмування, а саме, функції reduce, map, lambda;
#  4-ий варіант: застосувати функцію sum;

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
listik = input("Введіть строку: ").split(' ')
a = reduce(reducer, listik)
print(list(a))


def sum(text):
    list = text.split(' ')
    result = []
    for element in list:
        for part in element:
            result.append(part)
    return result
text = input("Enter: ")
print(sum(text))
