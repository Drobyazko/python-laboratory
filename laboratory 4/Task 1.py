n=0
while n!=1:
    print("Enter a that is a number")
    a=int(input())
    print("Enter b that is a number")
    b = int(input())
    print("Enter c that is a number")
    c = int(input())
    print("Enter d that is a number")
    d=int(input())
    list=[a, b, c, d]
    import itertools
    for element in range(3, len(list)):
        for subset in itertools.permutations(list, element):
            x = int(subset[0])
            y = int(subset[1])
            z = int(subset[2])
            if (z < x + y) and (x< z + y) and (y < x + z):
                p = (x + y + z) / 2
                import math
                print(round(math.sqrt(p * (p - x) * (p - y) * (p - z)),3))
    print("Enter 1 to stop and 0 to continue")
    n = int(input())