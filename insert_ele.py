def inserting(num,list,num1,num2):
       list[num1]=num2
       print()

num=int(input("enter the list limits : "))
list=[]
print("enter the values : ")
for i in range(num):
    number=int(input())
    list.append(number)
print("your entered the list is : ",list) 
num1=int(input("enter the index number to insert  : "))   
num2=int(input("enter the number to insert  : "))   

inserting(num,list,num1,num2)