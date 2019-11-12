import re
import sys
def int_input(text):
    pattern = r"^[-\d]\d*$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введите целое число: ")
    return int(user_input)

def Right():
    l = int(input("Введите длину: "))
    s = input("Введите строку: ")
    print(f" "*l, s)
    a = int(input("Введите 1 если хотите повторить, 0 для завершения "))
    if a == 1:
        Right()
    elif a == 0:
        sys.exit(0)