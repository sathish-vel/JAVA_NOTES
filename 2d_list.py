
# r=int(input("enter the rows : "))
# c=int(input("enter the columns : "))
# print("enter the element in 1st array : ")
# A=[]
# for i in range(r):
#     list=[]
#     for j in range(c):
#         list.append(int(input()))
#     A.append(list)
# for i in range(r):
#     for j in range(c):
#         print(A[i][j],end="  ")
#     print()    

# print("enter the element in 2nd array : ")    
# B=[]
# for i in range(r):
#     list1=[]
#     for j in range(c):
#         list1.append(int(input()))
#     B.append(list1)
# for i in range(r):
#     for j in range(c):
#         print(B[i][j],end="  ")
#     print()    

# result=[]
# for i in range(r):
#     list2=[]
#     for j in range(c):
#         list2.append(0)
#     result.append(list2)
# for i in range(r):
#     for j in range(r):
#         for k in range(r):
#             result[i][j]+=A[i][k]*B[k][j]
# print("MATRIX MULTIPICATION IS : \n")            
# for i in result:
#     print(i) 
# print("------INSERT THE ELEMENT-------")    
# print("enter the index element : ")     
# n1=int(input())      
# n2=int(input())    
# n3=int(input("enter the element to insert :"))
# for i in range(r):
#     for j in range(r):
#         result[n1][n2]=n3 
#         print(result[i][j],end=" ")
#     print()

# print("------SEARCHING ELEMENT OF INDEX------- : ")
# n4=int(input("enter the element : "))
# if n>0:
#     for i in range(r):
#         for j in range(r):
#             if n4==result[i][j]:
#                 print(i,j,end="")
#                 break
#         else:
#             print("invalid")

n=int(input("enter the number(2 : 2x2 matrix) : "))
A=[]
print("enter the first matrix : ")    

for i in range(n):
    list=[]
    for j in range(n):
        list.append(int(input()))
    A.append(list)
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()    
print("enter the second matrix : ")    
B=[]
for i in range(n):
    list=[]
    for j in range(n):
        list.append(int(input()))
    B.append(list)
for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")
    print()    
result=[]
for i in range(n):
    list=[]
    for j in range(n):
        list.append(0)
    result.append(list)
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j]+=A[i][k]*B[k][j]
print("matrix of multiplication : ")        
for i in range(n):
    for j in range(n):
        print(result[i][j],end=" ")        
    print()    
# for i in result:
#     print(i)   
print("enter the index valuev : ")
n1=int(input())
n2=int(input())
n3=int(input("enter the element to insert : "))
for i in range(n):
    for j in range(n):
        result[n1][n2]=n3
        print(result[i][j],end=" ")
    print()
print("enter the index value")
n4=int(input())
n5=int(input())
print(result[n4][n5])
n6=int(input("enter the element : "))
if n6>0:
    for i in range(n):
        for j in range(n):
            if result[i][j]==n6:
                print(i,j,end="")
else:
    print("invalid")    























