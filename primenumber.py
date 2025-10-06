def primenumber(x):
    for i in range(2,x):
        if(x%i==0):         
            print("it is a composite number")
            break
    else:  
        print("prime number")
        
        
            
a=int(input("enter a number: "))
primenumber(a)
