# Задача: Обчислити добуток 1/x^2+i
from functools import reduce
print("Enter your list")
text = input()
first_list = text.split(',')
print(first_list)
i = 1
result = 1
for var in first_list:
    var = int(var)
    result *= 1/(var*var)+i
    i = i + 1
print( round (result, 3))
