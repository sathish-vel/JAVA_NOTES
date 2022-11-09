num=int(input("enter the limits : "))
list=[]
list_dub=[]  
length=0  
for i in range(1,num+1):
    dub=int(input())
    list.append(dub)
n=int(input("enter the repeated number : "))    
for i in range(1,num+1):
    if i==n:
        length+=1
else:
    print("invalid")
print(n,"appears",length,"times in given list")    