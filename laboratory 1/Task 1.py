"""""""""""
З тризначного числа x відняли його останню цифру.
Коли результат розділили на 10, а до приватного зліва приписали останню цифру числа x, то вийшло число 237. Знайти число x.
"""""""""""
print("Введіть додатє тризначне число")


# a = True
# while a:
#     number = str(input())
#     if (not number.isdigit()):
#         print ("srt is NOT Digit")
#     else:
#         if (not (99<int(number) & int(number)<1000)) :
#             print ("chage number")
#         else:
#             a = False


# import re
# user_input = input()
# def number(x):
#     pattern = "^(\d{3})$"
#     while not re.match(pattern, user_input):
#         user_input = input("Введене значення некоректне , Введіть число:")
#     return number(user_input)
#     print("Str is digit")
#     return number(input())
#     a = int(number[0])
#     b = int(number[1])
#     c = int(number[2])
#     z = int(str(b) + str(c))
#     x = 10*z+a
#     return number(x)
#
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
Програма написана для будь-якого тризначного числа. універсальна
"""""""""""