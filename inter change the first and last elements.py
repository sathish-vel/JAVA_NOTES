def inter_change_list(num):
    list=[]
    for i in range(num):
        dub=int(input())
        list.append(dub)
    print("Your Original List is : ",list)    
    temp=list[0]
    list[0]=list[len(list)-1]
    list[len(list)-1]=temp
    print("After inter change the first & last element : ",list)     
num=int(input("enter the limits : "))
inter_change_list(num)

