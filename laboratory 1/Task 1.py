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


import re
def number(x):
    pattern = "^(\d{3})$"
    user_input = input()
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне , Введіть число:")
    return number(user_input)
    print ("Str is digit")
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])
    z = int(str(b) + str(c))
    x = 10*z+a
    return number(input())
print(number(input()))
"""""""""""
Програма написана для будь-якого тризначного числа. універсальна
"""""""""""