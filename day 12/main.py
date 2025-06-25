import random
print("Welcome to The Number Guessing Game! ")
print("Let me think the number \n")
random_number = random.randint(1, 101)

difficulty = input("Choose a difficulty (eg. easy, medium, hard): ")


def game(difficulty):
    if difficulty == "easy":
        num = 10
        print(f"You will get {num} attempts to guess the number.")
        guessing_game(num)


    elif difficulty == "medium":
        num = 7
        print(f"You will get {num} attempts to guess the number.")
        guessing_game(num)



    elif difficulty == "hard":
        num = 5
        print(f"You will get {num} attempts to guess the number.")
        guessing_game(num)


def guessing_game(num):
    """ in this part he is whole functionality of the game of guessing game"""
    while num > 0:
        print("Guess the number")
        guess_number = int(input("Guess a number between 1 and 100: "))

        if guess_number == random_number:
            print(f"\nCongratulations, you won! {guess_number}!")
            break

        elif guess_number > random_number:
            print(f"\nSorry, number is high {guess_number}.")
            num = num - 1
            print(f"attempt left {num}")

        else:
            print(f"\nSorry, number is low {guess_number}.")
            num = num - 1
            print(f"attempt left {num}")

        if num == 0:
            print(f"Sorry , you lose number is {random_number}")

game(difficulty)



