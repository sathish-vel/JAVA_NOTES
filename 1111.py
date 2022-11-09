# s=int(input("enter the staring limit "))
# e=int(input("enter the ending limit "))
# limits=int(input("enter the limits "))
# a=s-2
# b=s-1
# sum=0
# for i in range(s,e+1):
#     c=a+b;
#     a=b
#     b=c
#     if c<=e:
#         print(c,end=" ")
#     count=0
#     for i in range(1,e+1):
#         if c%i==0:
#             count+=1
#     if count==2:
#         if c<=e:
#             print(c,end=" ")      
#             sum+=c  
# print("\nthe prime finbonacci sum is :",sum)
# if limits>sum:
#     print("yes!")
# else:
#     print("no!")
# n=5
# for i in range (n,1,-1):
#     for s in range(1,n-i+1):
#         print("  ")
#         for j in range(1,i):
#                 print("* ",end="  ")
#         print("\n")    


n=int(input("enter the limit : "))
n1=int(input("enter the limit : "))
for i in range(n,n1+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")
   

