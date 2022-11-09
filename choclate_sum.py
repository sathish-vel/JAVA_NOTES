rupees=int(input())
choclate=rupees
wrapper=choclate

while wrapper > 1:
    if wrapper%3==0:
        wrapper=wrapper//3
        choclate=choclate+wrapper
    else:
        reminder=wrapper%3
        wrapper=wrapper//3
        choclate=choclate+wrapper
        wrapper=wrapper+reminder
print("Totally",choclate,"choclates you can buy....")





   


