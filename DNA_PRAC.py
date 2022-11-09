# sum=0
# dna="abcd"
# dna1=[]
# for i in dna:dna1.append(i)
# gene="cdaa"
# gene1=[]
# for i in gene:gene1.append(i)

# health=[2,3,4,5,6]
# for i in range(len(dna1)):
#     for j in range(len(gene1)):
#         if dna1[i]==gene1[j]:
#             sum=sum+health[j]
#             print(health[j],gene1[j])
# print(sum)

str="xyz"
str1=list(str)
list=[]
count=0
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if str1[i]==str1[j]:
            new=str1[i]+str1[i]
            list.append(new)
            count+=1
            break
        else:
            if i==len(str1)-2:
                list.append(str1[j])
            else:
                # if str1[i]==str1[j]:
                list.append(str1[i])
                break    

          
print(list)            
print(count)            