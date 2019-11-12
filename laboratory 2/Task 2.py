"""""""""""
Скласти програму розкладання натурального числа n на прості множники.
"""""""""""
i = True
while (i):
    my_number = str (input())
    if (not my_number.isdigit()):
        print ("change input value")
    else:
        my_number = int(my_number)
        i = False
for y in range(1, my_number+1):
    if(my_number%y==0):
        print(y)
