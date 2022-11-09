#GENE
num=int(input("Enter The No of GENES : "))
gene=[]
for i in range(num):
    gene.append(input())
print(gene)

#HEALTH    
print("Enter The {} Health Values : ".format(num))
health=[]
for i in range(num):
    health.append(int(input()))
print(health) 

#DNA
dna=int(input("enter the no of DNA : "))
s,e,d=[],[],[]
for i in range(dna):
    s.append(int(input("enter the Starting health value : ")))#starting Range
    e.append(int(input("enter the Ending health value   : ")))#Ending Range
    d.append(input("enter the DNA                   : "))#DNA
# print(s[0],e[0])
# print(s[1],e[1])
# print(s[2],e[2])
# print(d)

gene1=gene[s[0]:e[0]+1]
health1=health[s[0]:e[0]+1]
# print(gene1)
# print(health1)

d=str(d)
new_dna=[]
count=0
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if d[i]==d[j]:
            n=d[i]+d[j]
            new_dna.append(n)
            count+=1
            count1=count
            break
        else:
            if i==len(d)-2:
                new_dna.append(d[j])
            else:
                new_dna.append(d[i])
            break    
sum=0
print("the new     : ",new_dna)
count1=count
if count1==2:
    # for dna1 in new_dna:
        for j in range(len(new_dna)):
            for k in range(len(gene1)):
                if new_dna[j]==gene1[k]:
                    sum=sum+health1[k]
                    print(health1[k],gene1[k])
        print("The Total Health of \"{}\" is {}".format(str(d),sum))
elif count==0:    
    for dna1 in d:
        for j in range(len(dna1)):
            for k in range(len(gene1)):
                if dna1[j]==gene1[k]:
                    sum=sum+health1[k]
                    print(health1[k],gene1[k])
    print("The Total Health of \"{}\" is {}".format(str(d),sum))