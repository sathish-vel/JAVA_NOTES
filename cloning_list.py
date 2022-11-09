num=int(input("enter the limits : "))
list=[]
list_dub=[]  
length=0  
for i in range(1,num+1):
    dub=int(input())
    list.append(dub)
    length+=1
print("your original list is : ",list)    
for i in list:
    list_dub.append(i)
print(list_dub)    
for i in range(length-1,0-1,-1):
    print(list_dub[i],end=",")