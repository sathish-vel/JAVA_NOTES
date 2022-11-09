def reverse_number(num):
    result=0
    n=num
    count=0
    while num>0:
        rem=num%10
        result=result*10+rem
        num//=10
        count+=1
    print("number count is : " +str(count))    
    print("the reverse number is :" +str(result))    
    if result==n:
        print("it is a reversed number.")
    else:
        print("it is a NOT a reversed number.")    
num=int(input("enter the number : "))
reverse_number(num)