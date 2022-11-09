num=int(input("enter the number : "))
count,length=0,0
list=[]
while 0<num:
    rem=num%2
    list.append(rem)
    num=num//2
    length+=1
    print()
    if rem==1:
        count+=1

print("STRING SLICE USING PRINTING BINARRY NUMBER IS :")        
print(list[::-1])    
print("FOR LOOP USING PRINTING BINARRY NUMBER IS : ")
for i in range(length-1,-1,-1):
    print(list[i],end=" ")
print("\nTOTAL ONE'S COMPONENT IN GIVEN NUMBER IS : ",count)        
print("THE BINARY NUMBER LENTH IS  :",length)    
