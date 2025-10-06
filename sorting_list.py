num=int(input("enter number of entreies: "))
lst=[]
for i in range(num):
    roll=int(input("enter roll no: "))
    name=input("enter name: ")
    rec=[roll,name]
    lst.append(rec)
print(lst)
for i in range(len (lst)):
    for j in range(i+1,len(lst)):
        if lst[j][0]<lst[i][0]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)






