import random
from art import logo
game_start=input("Do u you want to play a game of Blackjack type 'y' or 'n' ").lower()

card_values = {
"Ace": [1, 11],
"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ("King", "Queen", "Jack", "10"): 10
}
your_cards =[]
pc_cards=[]
if game_start=="y":
    print(logo)
    random_card1 = random.sample(list(card_values.values()),2)
    your_cards.append(random_card1)
    random_card2 = random.sample(list(card_values.values()), 2)
    pc_cards.append(random_card2)
    your_card_score=sum(your_cards[0])
    pc_card_score=sum(pc_cards[0])
    print(f"Your cards:{your_cards[0]} and the score is:{your_card_score} " )
    print(pc_cards[0])
    print(f"Computer's first card:{pc_cards[0][0]}")
    while your_card_score <21:
        withdraw_card = input("Type another 'y' to get another card or,type 'n' to pass ").lower()
        if withdraw_card=="y":
            withdraw_another=random.choice(list(card_values.values()))
            your_cards[0].append(withdraw_another)
            your_card_score=sum(your_cards[0])
            print(f"Your cards:{your_cards[0]} and the score is:{your_card_score} ")
        else:
            print(f"Your final hand:{your_cards[0]},final score:{your_card_score} ")
            break
    if pc_card_score<21:
        withdraw_another2=random.choice(list(card_values.values()))
        print(withdraw_another2)
        pc_cards[0].append(withdraw_another2)
        pc_card_score=sum(pc_cards[0])
        print(f"Computer's final hand:{pc_cards[0]},final score:{pc_card_score}")
    else:
        print(f"Computer's final hand:{pc_cards[0]},final score:{pc_card_score}")
    if pc_card_score==21 and your_card_score==21:
        if pc_card_score==your_card_score:
            print("Its a Draw :D")
    if pc_card_score==21 and your_card_score!=21:
        if your_card_score < pc_card_score in range(22):
            if your_card_score >=22 and pc_card_score <=21:
                print("You Lost!!!")
    if your_card_score==21 and pc_card_score!=21:
        if your_card_score > pc_card_score in range(22):
            if pc_card_score>=22 and your_card_score<=21:
                print("You Won!!!")





