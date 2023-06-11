# write a program using while loop to display character from string and if space then terminate.
x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))
z=int(input("enter the value of z: "))

if x>y>z:
    print(x,"is grater than",y,"and",z)
elif y>x>z:
    print(y,"is grater than",x,"and",z)
else:
    print(z,"is the gratest of all....") 