# З тризначного числа x відняли його останню цифру.
# Коли результат розділили на 10, а до приватного зліва приписали останню цифру числа x, то вийшло число 237. Знайти число x.
print("Введіть додатє тризначне число")
a = True
#while not str(input()).isdigit():
while a:
    number = str(input())
    if (not number.isdigit()):
        print ("srt is NOT Digit")
    else:
        if (not (99<int(number) & int(number)<1000)) :
            print ("chage number")
        else:
            a = False

print ("Str is digit")
a = int(number[0])
b = int(number[1])
c = int(number[2])
z = int(str(b) + str(c))
x = 10*z+a
print(x)
# Програма написана для будь-якого тризначного числа. універсальна

