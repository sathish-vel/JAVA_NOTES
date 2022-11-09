# row=int(input("enter the row : "))
# for i in range(1,row+1):
#         for k in range(1,row-i+1):
#             print("  ",end=" ")
#         for j in range(1,i+1):
#             if( j==row-i+1 or i==row or j==row):
#                 print(" *",end=" ")
#             else:
#                 print("  ",end=" ")    
#         print()    
name=str(input("enter a name : "))
len=len(name)-1
for i in range(len,-1,-1):
    new[i]=list1[i]

