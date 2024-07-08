def add(x,y):
    return x + y

a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
d=int(input("Enter value of d = "))

e=add(a,b)
f=add(c,d)
print("Add a+b = ",e)
print("Add c+d = ",f)
print("Add a+b+c+d = ",add(e,f))