def prime_number(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("it is a prime number  ")
    else:
        print("it is NOT a prime number  ")
# num=int(input("enter the number : "))
# prime_number(num)

def prime_number_given_range(num):
    print("the given range prime numbers:")
    for i in range(20,num+1):
        count=0
        for j in range(1,num+1):
            if i%j==0:
                count=count+1
        if count==2:
            print(i,end=",")
num=int(input("enter the number : "))
prime_number(num)
prime_number_given_range(num)
