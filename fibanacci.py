def fibanacci(num,n):
    a,b=0,1
    print("0,1 are fibanacci starting numbers.")
    for i in range(1,num):
        c=a+b
        a=b
        b=c
        if c<num:
         print(c,end=",")
         if n==c:
            print("it is a fibanacci number.")
num=int(input("enter the limits : "))
n=int(input("enter the fibanacci number : "))

fibanacci(num,n)