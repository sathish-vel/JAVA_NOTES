n=int(input("enter a number : "))
# n=long(n)
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:print("not a palindrome")
else:print("not a palindrome")         
