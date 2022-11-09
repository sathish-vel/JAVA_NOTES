d1,d2="145614",14
# d1,d2="2352",2
num=' '
s,s1=3,4
for i in d1:
    i=num+i
    i=int(i)
    if i>=d2:
        r=i%d2
        q=i//d2
        d3=q*d2
        print("{})  {}".format(d2,d1))
        print(" "*s1,"*"*len(d1))
        print(" "*s, i)
        print(" "*s, d3)
        num=' '
        s+=2
        if i-d3!=0:
            minus=i-d3
            num=str(minus)
    else:
        num=str(i)
