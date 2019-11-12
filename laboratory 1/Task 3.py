# Знайти функцію для якої спосіб знаходження значення залежить від області визначення
print ("Введіть число")
a = True
while a:
    x = str(input())
    if (not x.isdigit() and not x[0]=="-"):
        print ("change input value. we need number")
    elif (x[0]=="-" and x[1:].isdigit):
        a = False
    elif (x=="0"):
        a = False
    elif (x.isdigit()):
        a = False
x = int(x)
if (x<=2):
    y=x*x+4*x+5
    print (y)
if (x>2):
    y=1/(x*x+4*x+5)
    print (y)