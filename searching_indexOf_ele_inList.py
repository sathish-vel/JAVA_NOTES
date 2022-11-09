def searching(num,list,num1):
    for i in range(num):
        if list[i]==num1:
            print(i)
num=int(input("enter the list limits : "))
list=[]
print("enter the values : ")
for i in range(num):
    number=int(input())
    list.append(number)
print("your entered the list is : ",list) 
num1=int(input("enter the searching element : "))   
searching(num,list,num1)