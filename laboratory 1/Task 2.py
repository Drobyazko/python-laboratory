i=0
print ("Enter your first number for check")
a = True
while a:
    number1 = str(input())
    if (not number1.isdigit() and not number1[0]=="-"):
        print ("change input value")
    elif (number1[0]=="-" and number1[1:].isdigit):
        i = i + 0
        a = False
    elif (number1=="0"):
        i = i + 0
        a = False
    elif (number1.isdigit()):
        i = i + 1
        a = False
print ("Enter your second number for check")
b = True
while b:
    number2 = str(input())
    if (not number2.isdigit() and not number2[0] == "-"):
        print ("change input value")
    elif (number2[0] == "-" and number2[1:].isdigit):
        i = i + 0
        b = False
    elif (number2=="0"):
        i = i + 0
        b = False
    elif (number2.isdigit()):
        i = i + 1
        b = False
print ("Enter your third number for check")
c = True
while c:
    number3 = str(input())
    if (not number3.isdigit() and not number3[0] == "-"):
        print ("change input value")
    elif (number3[0] == "-" and number3[1:].isdigit):
        i = i - 1
        c = False
    elif (number3=="0"):
        i = i + 0
        c = False
    elif (number3.isdigit()):
        i = i + 1
        c = False
print("Кількість додатніх: ", i)
