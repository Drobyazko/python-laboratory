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

