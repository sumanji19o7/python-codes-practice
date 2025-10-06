#factorial of a number:

def fact(n):
    product = 1
    if n == 0:
        print("factorial of number is: ",product)
    else:
        for i in range(1,n+1):
            product=product*i
    print("factorial is: ",product)
num=int(input("enter a number: "))
fact(num)
            
