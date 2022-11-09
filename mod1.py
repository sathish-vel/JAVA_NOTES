def fibanacci(x, y):
    a=0 
    b=1
    for i in range(x,y):
        c = a+b
        a = b
        b = c
        if c<=y:
            print(c,end=" ")


def reverse(n):
    sum=0
    while n > 0:
        rem=n%10
        sum=sum*10+rem
        n=n//10
    print("\n the reverse number is : " +str(sum))    


def dictionary():
    dic={
        "name":"satz",
        "age":'21',
        "gender":"male",
        "roll numner":'412218104029'
    }
    num=int(input("enter a number : "))
    print(dic)
    print(num)

