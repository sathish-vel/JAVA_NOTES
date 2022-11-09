import random
print("\t | ROCK PAPER SCISSOR GAME |  ")
chance=int(input("enter the no of chance do u want to play game : "))
data=['r','p','s']
user=0
computer=0
for i in range(chance):
    guest=random.choice(data)
    choice=input("\n enter the choice : ")
    if choice==guest:
        print("Computer Choosed : ",guest)
        print("Draw")
    elif choice=='r' and guest=='p':
        print("Computer Choosed : ",guest)
        print("Computer Win")
        computer+=1
    elif choice=='r' and guest=='s':
        print("Computer Choosed : ",guest)
        print("User Win")
        user+=1
    elif choice=='p' and guest=='r':
        print("Computer Choosed : ",guest)
        print("User Win")
        user+=1
    elif choice=='p' and guest=='s':
        print("Computer Choosed : ",guest)
        print("Computer Win")
        computer+=1
    elif choice=='s' and guest=='r':
        print("Computer Choosed : ",guest)
        print("Computer Win")
        computer+=1
    elif choice=='s' and guest=='p':
        print("Computer Choosed : ",guest)
        print("User Win")
        user+=1
print("\nThe Final Score Is : ") 
print("Your Score Is : ",user)
print("computer Score Is : ",computer)

