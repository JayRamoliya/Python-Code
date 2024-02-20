print("1. +")
print("2. -")
print("3. *")
print("4. /")

choice=int(input("enter your choice: "))
x=input("first number: ")
y=input("second number: ")

y=float(y)
x=float(x)

if choice==1:
    print(x+y)
elif choice==2:
    print(x-y)
elif choice==3:
    print(x*y)
elif choice==4:
    print(x/y)

print("your answer")


