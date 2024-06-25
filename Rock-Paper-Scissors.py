import random

u_score=0
c_score=0
while True:
    options=["Rock","Paper","Scissors"]
    print("your options is:--",options)
    user=input("enter options")
    computer=random.choice(options)
    if user.lower()!="rock" or user.lower()!="paper" or user.lower()!="scissors":
        if user.lower()==computer.lower():
            print("your game is tie!..")
        elif (user.lower()=="rock" and computer.lower()=="paper")or(user.lower()=="paper" and computer.lower()=="scissors") or(user.lower()=="scissors" and computer.lower()=="rock"):
            u_score+=1
        else:
            c_score+=1
    else:
        print("enter write options")

    if(u_score>c_score):
        print("you win","your score is:-",u_score)
    else:
        print("computer win","computer score is:-",c_score)

        
    print("if you want to play anothor round. ?( y/n)")
    again=input().lower()
    if again=="y":
        continue
    else:
        break
        


