def sum(text):
    list = text.split(' ')
    result = []
    for element in list:
        for part in element:
            result.append(part)
    return result
text = input("Enter: ")
print(sum(text))