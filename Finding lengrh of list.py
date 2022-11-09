def len_of_list(name):
    length=0
    for i in name:
        length+=1
    print("the length of the name is : ",length)

    list=[]
    for i in range(5):
        dub=input()
        list.append(dub)
    print(list)
    count=0
    for i in list:
        count+=1
    print(count)    
    print(list[0:2])    
name=input("enter the name : ")
len_of_list(name)