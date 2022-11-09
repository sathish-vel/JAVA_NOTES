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
#..................................................................................................       
def swap_two_element(num,pos1,pos2):
    list=[]
    for i in range(num):
        dub=int(input())
        list.append(dub)
    temp=list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    print(list)
###############################################################################################3
num=int(input("enter the limits : "))
inter_change_list(num)
print("PYTHON PROGRAM TO SWAP TO ELEMENTS IN A LIST : ")
pos1=int(input("enter the  position one : "))
pos2=int(input("enter the  position second : "))
swap_two_element(num,pos1,pos2)
