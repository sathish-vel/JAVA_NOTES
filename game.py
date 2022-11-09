import random
suit=["SP,","CL,","HR,","DM,"]
face=["2","3","4","5","6","7","8","9"]
result=[]
s=len(suit)-1
f=len(face)-1
# print(s,f)
for i in suit:
    list=[]
    for j in face:
        list=i+j
        result.append(list)
print("the deck : \n",result)        
x=[]
x.append(random.shuffle(result))
print("After shuffled deck \n",result)
sum=[]
for i in range(3):
    list=[]
    for j in range(3):
        list.append(random.choice(result))
    sum.append(list) 

print("WELCOME TO THE GAME! : ")
for i in range(3):
    for j in range(3):
        print(sum[i][j],end="|") 
    print() 
empty=[]    
for i in range(3):
    for j in range(3):
        empty.append(sum[i][j])
print(empty)        
# print("enter the index of the value to insert : ")

# y=[]    
# for i in result:
#     for j in empty:
#         if i==j:
#            break 
#     else:
#         y.append(i)
# print(y)

# n1,n2=int(input()),int(input())    
# n3=input("enter the element to insert : ")
# for i in range(3):
#     for j in range(3):
#         sum[n1][n2]=n3
#         print(sum[i][j],end="|")
#     print()  
for i in range(20):
    card_l=19-i
    score=i*(-1)
    print("score:",score)
    # print("card left : ",card_l)
    number=input("Deal or Done? ")
    if number=="Deal":
        New_card=random.choice(sum)
        New_card=random.choice(New_card)
        print(New_card)
    print("enter the index of the value to insert : ")
    n1,n2=int(input()),int(input())    
    for i in range(3):
        for j in range(3):
            sum[n1][n2]=New_card
            print(sum[i][j],end="|")
        print()  
