def factorial(num,sum):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial number is : "+str(sum))    
num=int(input("enter the number : "))
sum=1
factorial(num,sum)
