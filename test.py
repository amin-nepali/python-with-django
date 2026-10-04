a = 7
b = 3
c = 12

if a > 5:
    if b > 5:
        print("P")
    elif c > 10:
        if a + b > c:
            print("S")
        else:
            print("T")
    else:
        print("F")
elif c > a:
    print("U")
else:
    print("P")