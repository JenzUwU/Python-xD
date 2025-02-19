import random
from hangman_words import word_list
from hangman_art import stages,logo
print(logo)
game_over = False
placeholder=""
correct_letters=[]
chosen_word=random.choice(word_list)
for i in range(len(chosen_word)):
    placeholder += "_"
# print(placeholder)
lives=6
while not game_over:
        guess = input("Guess a letter:").lower()
        if guess not in chosen_word:
            lives-=1
            print("*************incorrect guess************")
        if guess in correct_letters:
            print("************************************You have already guessed it!!********************************************")
        display = ""
        for letter in chosen_word:
            if letter==guess:
                display+=letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display+=letter
            else:
                display+="_"
        print(f"Word to guess: {display}")
        print(f"**********************************You have {lives}/6 Lives left!!****************************************")
        print(stages[lives])

        if "_" not in display:
            game_over = True
            print("*************************************YOU WON******************************************")
            break
        elif lives==0:
            print("*******************************************YOU LOST*********************************************")
            print(f"The correct word was {chosen_word}")
            break

