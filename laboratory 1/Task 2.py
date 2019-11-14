"""""""""""
Підрахувати кількість додатних серед чисел а, b, с (ввести з клавіатури).
"""""""""""
import re
def validator(pattern,promt):
    number = input(promt)
    while not bool(pattern.match(number)):
        print("Enter new: ")
        number = input(promt)
    return number
re_integer = re.compile('^[+-]{0,1}\d+\.{0,1}\d+$')

def in_put(promt):
    number = int(validator(re_integer,promt))
    return number
def main():
    counter = 0
    list = [a, b, c]
    for element in list:
        if element>0:
            counter+=1
        else:
            counter+=0
    return counter
a = in_put("Enter your first number for check: ")
b = in_put("Enter your second number for check: ")
c = in_put("Enter your third number for check: ")
print(main())