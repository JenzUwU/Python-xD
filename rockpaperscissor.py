import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

r="Rock"
p="Paper"
s="Scissors"
while True:
    human_chose= int(input("\nWhat do you choose? \n # Type 0 for Rock \n # Type 1 for scissors \n # Type 2 for paper :D "))





    if human_chose==0:
        print(f"You chose: {r} \n {rock}")
    elif human_chose==1:
        print(f"You chose: {p} \n {paper}")
    elif human_chose==2:
        print(f"You chose: {s} \n {scissors}")
    else:
        print("Enter 0 or 1 or 2 only :<")


    computer_chose=random.randrange(0,3)

    if computer_chose==0 and human_chose<=2:
        print(f"Computer chose: {r} \n {rock}")
    elif computer_chose==1 and human_chose<=2:
        print(f"Computer chose: {p} \n {paper}")
    elif computer_chose==2 and human_chose<=2:
        print(f"Computer chose: {s} \n {scissors}")
    else:
        print("")

    if computer_chose==0 and human_chose==0:
        print("You Tied")
    elif computer_chose==0 and human_chose==1:
        print("You Won")
    elif computer_chose==0 and human_chose==2:
        print("Computer Won")
    elif computer_chose==1 and human_chose==0:
        print("You Won")
    elif computer_chose==1 and human_chose==1:
        print("You Tied")
    elif computer_chose == 1 and human_chose == 2:
        print("You Won")
    elif computer_chose==2 and human_chose==0:
        print("You Won")
    elif computer_chose==2 and human_chose==1:
        print("Computer Won")
    elif computer_chose==2 and human_chose==2:
        print("You Tied")
