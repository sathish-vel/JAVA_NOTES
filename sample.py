import random

# r = int(input("enter the rows : "))
# c = int(input("enter the colunms : "))
# matrix = []
# for i in range(r):
#     array = []
#     for j in range(c):
#         new = int(input())
#         array.append(new)
#     matrix.append(array)
# print(matrix)
print("\n---------------------------")
suit = ["SH", "CL", "HR", "DM"]
a = []
for i in suit:
    for j in range(2, 10):
        # a.append("["+i+","+str(j)+"]")
        a.append(i+str(j))

print(a)
print("+++++")

y=[]
for i in range(9):
    x=random.choice(a)
    y.append(x)
    

print(")))))))))))))))))))")
print(y)
# for i in range(1,10):
#     print(random.choice(a),end=" ")
# print("\n---------------------------")
# for i in range(9):
    # b=[]
    # b.append(a[i])
    # print(b,end="")
    # print(a[i],end=" ")


    # print(a[i],end=",")