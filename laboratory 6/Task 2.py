# Виконати обробку елементів прямокутної матриці A, що має n рядків і m стовпців.
# Визначити, скільки від’ємних елементів міститься в кожному стовпці і в кожному рядку матриці.
# Результат оформити у вигляді матриці з  n+1 рядків і  m+1 стовпців.

import re
matric = []
result_in_stolbets = []
print("If you wat to enter stolets enter 1. if you don't print 0")
n = input()
while n != 0:
    print("Enter yor stolbets: ")
    stolbets = input().split(" ")
    matric.append(stolbets)
    print("If you wat to enter stolets enter 1. if you don't print 0")
    n = input()
if n == 0:
    print(result_stolbets(result_in_stolbets, matric))

def result_stolbets(result_in_stolbets, matric):
    for stolbets in matric:
        for element in stolbets:
            if element[0] == "-" and element[1:].isdigit():
                result_in_stolbets = +1
            else:
                result_in_stolbets = +0
    return result_in_stolbets




