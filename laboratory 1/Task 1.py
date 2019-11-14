"""""""""""
З тризначного числа x відняли його останню цифру.
Коли результат розділили на 10, а до приватного зліва приписали останню цифру числа x, то вийшло число 237. Знайти число x.
"""""""""""
import re
def number(num):
    return bool(re.match('^\d{3}$',num))
def number_new():
    num = input('Enter number: ')
    while not number(num):
        num = input('Enter again: ')
    return main(num)
def main(num):
    num=list(num)
    # num[0],num[1],num[3]=num[1],num[3],num[0]
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    z = int(str(b) + str(c))
    x = 10*z+a
    return x
print(number_new())
"""""""""""    
Програма написана для будь-якого тризначного числа. універсальна пр
"""""""""""