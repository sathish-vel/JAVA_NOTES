# list=[7,3,1,8,2,10]
# even=[]
# odd=[]
# for i in list : 
#     if i%2==0 : 
#         even.append(i)
#     else :
#         odd.append(i)
# print(even)            
# print(odd)

# for i in range(len(even)):
#     for j in range(i+1,len(even)) :
#         if even[i]>even[j]:
#             even[i],even[j]=even[j],even[i] 
# print(even)            
# print("the la minimum even no is : ",even[0])            

# for i in range(len(odd)):
#     for j in range(i+1,len(odd)) :
#         if odd[i]>odd[j]:
#             odd[i],odd[j]=odd[j],odd[i] 
# print(odd)             
# print("the la maxmimun odd no is : ",odd[-1])            




# n=3
# m=n
# for i in range(n):
#     for j in range(n-i):
#         print("* ",end="")
#         for k in range(n-m*2):
#             print("   ",)
#             m=m-1
#             for l in range(n-i):
#                 print("* ",end="")    
#     print("\n")        


#count the non vowels and printh the counts : 
str="vowels are counts and nonvowels ocuurance"

list1=[]
count=0

for i in str:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i==' ' ):
        flag=0
    else:
        list1.append(i)   
list1=list(dict.fromkeys(list1))
print(list1)
for i in list1:
    count=0
    for j in str:
        if i==j:
            count=count+1
    print(i,":",count,end=", ")
  

