a=[1,2,3,4,5,6]
b=[1,2,3]
c=[]
count=0
for i in a:
    for j in b:
        if i==j:
            count+=1
       
# print(count)
for i in range(count,6):
    print(a[i])
