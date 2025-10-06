import pickle
import time
def filecreate():
    num=int(input('enter number of students: '))
    f=open('stu.dat','wb')
    for i in range(num):
        
        name=input('enter name: ')
        roll=int(input('enter roll no: '))
        l=[roll,name]
        pickle.dump(l,f)
    f.close()


def reading():
    f=open('stu.dat','rb')
    while True:
        try:
            s=pickle.load(f)
            print(s)
        except EOFError:
            break
        time.sleep(0.5)
    f.close()

def searching():
    f=open('stu.dat','rb')
    name=input("enter name: ")
    num=int(input('enter roll number: '))
    
    try:
        while True:
            s=pickle.load(f)
            if s[0]==num and s[1]==name:
                print('record found',s)
                break
            else:
                pass
                
    except EOFError:
        f.close() 

    

def adding():
    f=open('stu.dat','ab')
    num=int(input('enter number of enteries: '))
    for i in range(num):
        name=input('enter name: ')
        roll=int(input('enter roll number: '))
        l=[roll,name]
        pickle.dump(l,f)
    print("records added successfully")
    f.close()

def deleting():
    f = open('stu.dat', 'rb')

    name = input('enter name to be deleted: ')
    roll = int(input('enter roll number to be deleted: '))
    target = [roll, name]
    whole = []

    while True:
        try:
            s = pickle.load(f)
            whole.append(s)
        except EOFError:
            f.close()
            break
    
    s=open('stu.dat','wb')
    for a in whole:
        if a[0]!=target[0] and a[1]!=target[1]:
            pickle.dump(a,s)
    print(whole)

def sorting():
    print("helloji")
    whole=[]
    f=open("stu.dat","rb")
    while True:
        try:
            s=pickle.load(f)
            whole.append(s)
        except EOFError:
            f.close()
            break
    print (whole)
    f.close()
    for i in range(len (whole)):
        for j in range(i+1,len(whole)):
            if whole[j][0]<whole[i][0]:
                whole[i],whole[j]=whole[j],whole[i]
    x=open("stu.dat","wb")  
    for i in whole:
        pickle.dump(i,x)
        print(i)
        time.sleep(0.5)
    f.close()
    
    


def menu():
    while True:
        print('enter write to enter new data')
        print('enter read to view data')
        print('enter search to search record')
        print('enter add to add record')
        print('enter sort to sort the records')
        print('enter delete to delete a record')
        print('enter quit to exit')
        print()
        choice=input('enter choice: ')
        if choice.lower()=='read':
            reading()
            
        elif choice.lower()=='write':
            filecreate()
            time.sleep(1)
        elif choice.lower()=='search':
            searching()
            time.sleep(1)
        elif choice.lower()=='add':
            adding()
            time.sleep(1)
        elif choice.lower()=='delete':
            deleting()
            time.sleep(1)
        elif choice.lower()=='sort':
            sorting()
            time.sleep(1)
        elif choice.lower()=='quit':
            print('program ended')
            time.sleep(1)
            break
            
        else:
            print('please enter correct choice!!')
            print()
        
        time.sleep(1)

menu()