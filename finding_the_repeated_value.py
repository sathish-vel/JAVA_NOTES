def repeat_val(list,num):
    new_l=[]
    count=0
    for i in range(num):
        for j in range(i+1,num):
            if list[i]==list[j]:
                print(list[i])
num=int(input("enter the limits : "))
list=[]
for i in range(num):
    number=int(input())
    list.append(number)
print("your list is : ",list_dub)
repeat_val(list,num)
