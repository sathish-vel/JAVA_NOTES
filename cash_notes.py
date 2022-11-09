num=int(input("enter the Amount : "))
tot_amount=num
cash_10=cash_500=cash_200=cash_1=cash_100=cash_50=cash_20=0
if tot_amount>=500:
    cash_500=tot_amount//500
    balance=tot_amount-(cash_500*500)
if balance>=200:
    cash_200=balance//200
    balance=balance-(cash_200*200)
if balance>=100:
    cash_100=balance//100
    balance=balance-(cash_100*100)
if balance>=50:
    cash_50=balance//50
    balance=balance-(cash_50*50)
if balance>=20:
    cash_20=balance//20
    balance=balance-(cash_20*20)
if balance>=10:
    cash_10=balance//10
    balance=tot_amount-(cash_10*10)
print("the total 500 notes is : "+str(cash_500))
print("the total 200 notes is : "+str(cash_200))
print("the total 100 notes is : "+str(cash_100))
print("the total 100 notes is : "+str(cash_50))
print("the total 100 notes is : "+str(cash_20))
print("the total 100 notes is : "+str(cash_10))




