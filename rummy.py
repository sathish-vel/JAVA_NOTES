import random
suit=["SP,","CL,","HR,","DM,"]
face=["2","3","4","5","6","7","8","9"]
arr=[]
for i in suit:
    list=[]
    for j in face:
        list=i+j
        arr.append(list)
print("the DECK is \n: ",arr) 

random.shuffle(arr)
print("After shuffled deck \n",arr)
sum=[]
for i in range(3):
    list1=[]
    for j in range(3):
        list1.append(random.choice(arr))
    sum.append(list1)    
print(sum[0][0])

for i in range(3):
    for j in range(3):    
        print(sum[i][j],end='|')
    print()    

empty=[]
for i in range(3):
    for j in range(3):    
        empty.append(sum[i][j])
print("Random cards : \n")
print(empty)

print("enter the index to insert the Value : ")
num1,num2=int(input()),int(input())
num3=input("enter the random cards : ")
num4=[]

for i in range(3):
    for j in range(3): 
        sum[num1][num2]=num3
        print(sum[i][j],end='|')
    print()    
print(sum[0][0])    