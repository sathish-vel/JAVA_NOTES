def max_element(list):
    max_element=list[0]
    for i in range(limit):
        if list[i]>max_element:max_element=list[i]
    print("the max element in the given list is : ",max_element)


def min_element(list):
    min_element=list[0]
    for i in range(limit):
        if list[i]<min_element:min_element=list[i]
    print("the min element in the given list is : ",min_element)
def sumOfTheElement(list): 
    sum=0
    for i in list:
        sum+=i
    print("the sum of the list is : ",sum)    

def accendin_and_deccending(list,limit):
    limit1=limit//2
    for i in range(limit):
        for j in range(i+1,limit):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    print("Sort first half in ascending order and second half in descending  :"  )
    for i in range(limit1):
        print(list[i],end=" ")
    for i in range(limit-1,limit1-1,-1):
        print(list[i],end=" ")

def finding_biggest_palindrome(list,limit):
    rev_list=[]
    palin_list=[]
    for i in list:
        sum=0
        while i>0:
            rem=i%10;
            sum=sum*10+rem
            i=i//10
        rev_list.append(sum)    
    for i in range(len(rev_list)):
        if list[i] == rev_list[i]:
            palin_list.append(list[i])
    for i in range(len(palin_list)):
        for j in range(i+1,len(palin_list)):
            if palin_list[i]>palin_list[j]:
                palin_list[i],palin_list[j]=palin_list[j],palin_list[i]
    print("\nLongest Palindrome in an List : ",palin_list[-1])
 
def Repeating_elements(list,limit):
    empty=[]
    for i in list:
        if i in empty:
            count=0
        else:
            empty.append(i)
    print(empty)



limit=int(input("enter the limits : "))
list=[]
for i in range(limit):
    list.append(int(input()))
print(list)    


max_element(list)
min_element(list)
sumOfTheElement(list) 
accendin_and_deccending(list,limit)
finding_biggest_palindrome(list,limit)
Repeating_elements(list,limit)