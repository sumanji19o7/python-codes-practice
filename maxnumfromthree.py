maximum=0
x,y,z=map(int,input("enter number: ").split())
if (x>y) and (x>z):
    maximum=x
elif (y>z) and (y>x):
    maximum=y
else:
    maximum=z
print("the max num is: ", maximum)
