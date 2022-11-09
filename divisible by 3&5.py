def divisible(num):
    for i in range(1,num+1):
        if i%3==0:
            if i<=num:
                print(i,end="  ")
    print(end="\n")
    for i in range(1,num+1):
         if i%5==0:
            if i<=num:
                print(i,end="  ")
num=int(input("enter the limits : "))
divisible(num)