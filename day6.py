# creating hangman game
import random

word_list = ["camel", "ox", "giraffe"]
#choosing the word by the user
choosen_word = random.choice(word_list)
print(choosen_word)

length = len(choosen_word)

stages = [
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / 
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |    
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |     |
     |    
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    
     |    
     |
    _|_
    """,
    """
     _______
     |     |
     |     
     |    
     |    
     |
    _|_
    """
]


blank =[]
place_holder = ""
for i in range(length):
    place_holder += "_"
    blank.append("_")
print(blank)

LETTER = []

game_over = False

life = len(choosen_word)

while life > 0 and not game_over :
    display = ""
    usr_letter = input("Guess a Word ").lower()
    cnt = 0
    for letter in choosen_word:

        if letter == usr_letter:
            blank[cnt] = letter
            display += letter
            LETTER.append(letter)
            print(display)
            print("right")

        elif letter in LETTER:
            display += letter

        else:
            display += "_"

        cnt = cnt + 1
    if usr_letter not in LETTER:
        life = life - 1
        print(stages[life])
        if life == 0:
            game_over = True
            print("you lose")


    if "_" not in display:
        game_over = True
        print("you win")


