list=[0,1,2,3,4,5,6,7,8,9]
# list=[]
# for i in range(0,9+1):
#     num=int(input())
#     list.append(num)
str=input("enter the list : ")
find=input("enter the number : ")
a=0
b=0
sum=[]
result=[]
for i in find:
    count=0
    for j in str:
        if i ==j:
           a=abs(a-count)
           break
        else:
           count+=1  
    b=b+a         
print(abs(b)) 