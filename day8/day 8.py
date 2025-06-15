from art_logo import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

print("Welcome to the secret auction program")
bidders = {}
def add_bidder():
    bidder_name = input("What is your name? ")
    bid = input("What is your bid? $")
    asking = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    bidders[bidder_name] = bid

    if asking == "yes":
        print("\n" * 108)
        add_bidder()

    else:
        # Get the highest bid amount
        highest_bid = max(bidders.values())

        # Get the bidder who made the highest bid
        winner = max(bidders, key=bidders.get)

        print(f"The winner is {winner} with a bid of ${highest_bid}.")


add_bidder()