def strong_number(num):
    n=num;
    result=0
    while n>0:
        rem=n%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i    
        result=result+fact
        n=n//10
    if result==num:
        print("the number is strong number.")
    else:
        print("the number is  NOT strong number.")
num=int(input("enter the number : "))
strong_number(num)