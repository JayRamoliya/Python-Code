a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))

if a<b:
    print(a, 'is less than', b)
    if c<b:
        print(c, 'is less than', b)
    else:
        print(c, 'is not less than', b)
else:
    print(a, 'is not less than', b)