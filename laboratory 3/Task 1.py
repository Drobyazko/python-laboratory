""""""""
"Програма має видалити літера а у слів, чия кількість літер дорівнює введеній"
""""""""
import re
def number(num):
    return bool(re.match('^\d+$',num))
def number_new():
    num = input('Enter number: ')
    while not number(num):
        num = input('Enter again: ')
    return main(num, text)
def main(num, text):
    num = int(num)
    text = text.split(' ')
    result = []
    for word in text:
        if (len(word) == num):
            result.append(word.lower().replace("а",""))
        else: result.append(word)
    return (' '.join(result))
text = (input("Enter text: "))
print(number_new())
