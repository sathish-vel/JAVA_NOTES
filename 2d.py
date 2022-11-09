num=int(input("enter the number (2:2*2=4).....:"))
list=[]
print("enter a 1st matrices : ")
for i in range(num):
    x=[]
    for j in range(num):
        n1=int(input())
        x.append(n1)
    list.append(x)
print(list)        
print("1st",num,"X",num,"matrix : ")
for i in range(num):
    for j in range(num):
        print(list[i][j],end=" ")
    print()    
list1=[]
print("enter a 2nd matrices : ")
for i in range(num):
    x=[]
    for j in range(num):
        n1=int(input())
        x.append(n1)
    list1.append(x)
print(list1)    
print("2nd",num,"X",num,"matrix : ")
for i in range(num):
    for j in range(num):
        print(list1[i][j],end=" ")
    print()    