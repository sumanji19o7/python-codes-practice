#programme to reverse a number
num=int(input("enter a number: "))
x=num
reversed=0
while x !=0:
    rem=x%10
    reversed= reversed*10 + rem
    x=x//10
print(reversed)