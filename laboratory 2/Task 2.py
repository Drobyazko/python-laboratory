"""""""""""
Скласти програму розкладання натурального числа n на прості множники.
"""""""""""
import re
def number(num):
    return bool(re.match('^\d+$',num))
def number_new():
    num = input('Enter number: ')
    while not number(num):
        num = input('Enter again: ')
    return main(num)
def main(num):
    num = int(num)
    for y in range(1, num + 1):
        if(num%y==0):
            print(y)
print(number_new())