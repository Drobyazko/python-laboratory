list1 = input("Enter list1 with ','").split(",")
list2 = input("Enter list2 with ','").split(",")
result1 = []
result2 = []
if len(list1)==len(list2):
    n = len(list1)
    for i in range(0,n):
        if list1[i]<=list2[i]:
            result1.append(list1[i])
        if list1[i] == list2[i]:
            result2.append()
        else: result2.append(list2[i])
print(result1)
print(result2)
