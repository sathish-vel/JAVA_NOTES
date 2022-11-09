def leap_year(num):
    if num%100==0:
        if num%400==0:
            print("it is leap year.")
        else:
            print("it is not a leap year.")
    elif num%4==0:
            print("it is leap year.")
    else:
        print("it is not a leap year.")
num=int(input("enter the leap year : "))
leap_year(num)
