num=int(input('enter a number: '))
for i in range (2,num):
    if num%i == 0:
        print('not a prime number!')
        continue
    else:
        print('its a composite number') 
        break

       


