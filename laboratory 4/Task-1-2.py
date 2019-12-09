string = str(input("Enter text: "))
t = str(input("Enter t: "))
def parse(string, t):
    rang = string.find(t)
    result1 = str(string[:rang])
    result2 = string[rang:]
    list = [result1, result2]
    return list
print(parse(string, t))