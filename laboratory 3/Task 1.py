text = ("А роза упала на лапу Азора")
text = text.split(' ')
print("Enter your n. "
      "Or print 0 if you don't want to continue")
n=1
while n!=0:
    n = int(input())
    if n not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print("Change value")
    else:
        n = int(n)
    n= int(n)
    result = []
    for word in text:
        if (len(word) == n):
            result.append(word.lower().replace("а",""))
        else: result.append(word)
    print(' '.join(result))
    result.clear()