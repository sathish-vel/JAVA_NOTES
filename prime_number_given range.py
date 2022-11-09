def prime_number(num1,num2,list):
    if num1==1:
        print(" 1 is not a prime number.\n you can enter 2 to ending value.")
    else:    
        for i in range(num1,num2) : 
            count=0
            for j in range(1,num2+1):
                if i%j==0:
                    count+=1
            if count==2:
                print(i,end=",")             
num1=int(input("enter the starting number "))
num2=int(input("enter the ending number "))
prime_number(num1,num2,list)

