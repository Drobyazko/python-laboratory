n = 0
while n!=1:
    print("Enter list")
    listik = input().split(' ')
    result = list("".join(listik))
    print (result)
    print("Enter 0 if you want to continue and 1 if you want to stop")
    n = int(input())