def swap_two_element(num,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    print("After swapping Two element in List : ",list)
num=int(input("enter the limits : "))
list=[]
for i in range(num):
    dub=int(input())
    list.append(dub)
print("your entered the list is : ",list)    
pos1=int(input("enter the first Index position one : "))
pos2=int(input("enter the  second Index position second : "))
swap_two_element(num,pos1,pos2)