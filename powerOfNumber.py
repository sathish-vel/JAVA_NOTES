def powerOfNumber(pow,base,count,result):
    for i in range(1,pow+1):
        result=result*base
        print(result)
    print("the power of base number is : " +str(result))
    

pow=int(input("enter the power : "))
base=int(input("enter the base : "))
count=0
result=1
powerOfNumber(pow,base,count,result) 
