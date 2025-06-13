import random

# Friend Picker
friends = ["ross", "chandler", "monica", "joey", "rachel", "phoebe"]
payer = random.randint(0, len(friends) - 1)
print(f'Bill is paid by {friends[payer]}')

# Rock Paper Scissors ASCII Art
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [Rock, Paper, Scissors]

computer = random.randint(0, 2)

# Get and convert player's input
player = input("Choose rock (0), paper (1), or scissors (2): ")

# Check for valid input
if player not in ['0', '1', '2']:
    print("Invalid input. Please choose 0, 1, or 2.")
else:
    player = int(player)

    print("\nPlayer chose:")
    print(rock_paper_scissors[player])

    print("Computer chose:")
    print(rock_paper_scissors[computer])

    # Decide winner
    if player == computer:
        print("It's a draw!")

    elif (player == 0 and computer == 2) or \
         (player == 1 and computer == 0) or \
         (player == 2 and computer == 1):
        print("Player wins!")

    else:
        print("Computer wins!")
