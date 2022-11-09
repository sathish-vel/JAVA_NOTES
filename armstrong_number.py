def armstrong(num):
    count=0
    sum=1
    n=num    
    arm=0
    result=num
    while num>0:            #find count value
        count=count+1
        num=num//10
    # print(count)
    while n>0:
        rem=n%10            #remainder
        for i in range(1,count+1):
            sum=sum*rem
        arm=arm+sum
        sum=1
        n=n//10
    print(arm)    
    if result==arm:
        print("the number is Armstrong. ")
    else:
        print("the number is not an Armstrong. ")

num=int(input("enter the number : "))
armstrong(num)

