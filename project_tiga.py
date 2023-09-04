#tugas 3   
x = int(input())
y = int(input())
z = int(input())
if(x>y):
    if(x>z):
        if (y>z):
            print(y)
        else:
            print(z)
if(y>x):
    if (y>z):
        if (x>z):
            print(x)
        else:
            print(z)
if(z>x):
    if (z>y):
        if (x>y):
            print(x)
        else:
            print(y)

