def sort(num,list):
    print("1. THIS IS SORT :")
    for i in range(num):
        for j in range(i+1,num):
            if list[i]>list[j]:
                # temp=list[i]
                # list[i]=list[j]
                # list[j]=temp
                list[i],list[j]=list[j],list[i]
    print("AFTER SORTING BUBBLE SORT : ",list)                
def bubble_sort(num,list):
    print("2. THIS IS BUBBLE SORT :")
    for i in range(num):
        for j in range(num-1):
            if list[j]>list[j+1]:
                    # temp=list[j]
                    # list[j]=list[j+1]
                    # list[j+1]=temp
                list[j],list[j+1]=list[j+1],list[j]
    print("AFTER SORTING BUBBLE SORT : ",list)                
num=int(input("enter the list limits : "))
list=[]
print("enter the values : ")
for i in range(num):
    number=int(input())
    list.append(number)
print("before sorting list : ",list)
sort(num,list)
bubble_sort(num,list)