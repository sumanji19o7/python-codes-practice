#fibonicci series
num=int(input("enter number: "))
x=0
y=1
i=0
print(x,y,end="  ")
while i!= (num-2):
    z=x+y
    y=z
    x=y
    i+=1
    print(z,end="  ")
"D:\Microsoft VS Code\Code.exe"