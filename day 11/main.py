from art import *
print(blackjack_art)

import random

print("welcome to the blackjack game")



cards = {
    "red_heart" : [1,2,3,4,5,6,7,8,9,10,10,10,10],
    "club" : [1,2,3,4,5,6,7,8,9,10,10,10,10],
    "spade" : [1,2,3,4,5,6,7,8,9,10,10,10,10],
    "diamonds" : [1,2,3,4,5,6,7,8,9,10,10,10,10]
}
keys = list(cards.keys())



dealer = 0
player = 0
taken_out_suits = {}



game_over = False

while not game_over:
    # Make a list of suits that still have cards left
    available_suits = [suit for suit in cards if len(cards[suit]) > 0]

    # If no cards left, end game
    if len(available_suits) < 2:
        print("No more cards! Game over.")
        break

    taken_out_suit_dealer = random.choice(available_suits)
    taken_out_suit_player = random.choice(available_suits)

    dealer_card = random.choice(cards[taken_out_suit_dealer])
    player_card = random.choice(cards[taken_out_suit_player])

    # Remove these cards from deck
    cards[taken_out_suit_dealer].remove(dealer_card)
    cards[taken_out_suit_player].remove(player_card)

    if taken_out_suit_player != taken_out_suit_dealer and dealer_card != player_card:

        print("player",taken_out_suit_player)
        player += player_card
        print(player ,"\n")

        print("dealer", taken_out_suit_dealer)
        dealer += dealer_card
        print(dealer,"\n")


    if dealer >= 21 :
        print("player wins!")
        game_over = True
    elif player >= 21 :
        print("dealer wins!")
        game_over = True



