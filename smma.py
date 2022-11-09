start_val=int(input("enter a starting value : "))
end_val=int(input("enter a starting value : "))
list=[]
for i in range(start_val,end_val+1):
    list.append(i)
print(start_val ,"to" ,end_val ,"is : ""\n",list)    
num1=int(input("enter the 1st number : "))
num2=int(input("enter the 2nd number : "))
if num1 >= start_val and num2 <=end_val:
    for i in range(num1,num2+1):
        print(i,end=",")
else:
    print("invalid")
