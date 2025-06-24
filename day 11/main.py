from art import *
import random

print(blackjack_art)

print("welcome to the blackjack game")
cards = {
        "heart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "club": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "spade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    }

def card_picking_dealer(cards):
    # Make a list of suits that still have cards left
    available_suits = [suit for suit in cards if len(cards[suit]) > 0]

    # If no cards left, end the game
    if len(available_suits) < 2:
        print("No more cards! Game over.")

    taken_out_suit_dealer = random.choice(available_suits)
    dealer_card = random.choice(cards[taken_out_suit_dealer])

    # Remove these cards from deck
    cards[taken_out_suit_dealer].remove(dealer_card)

    return taken_out_suit_dealer, dealer_card


def card_picking_player(cards):

    # Make a list of suits that still have cards left
    available_suits = [suit for suit in cards if len(cards[suit]) > 0]

    # If no cards left, end the game
    if len(available_suits) < 2:
        print("No more cards! Game over.")

    taken_out_suit_player = random.choice(available_suits)
    player_card = random.choice(cards[taken_out_suit_player])

    # remove cards that are already picked
    cards[taken_out_suit_player].remove(player_card)

    return taken_out_suit_player, player_card


dealer = []
player = []

game_over = False

while not game_over:

    taken_out_suit_player, player_card = card_picking_player(cards)
    taken_out_suit_dealer, dealer_card = card_picking_dealer(cards)

    if taken_out_suit_player != taken_out_suit_dealer and dealer_card != player_card:

        if player_card == 1 and sum(player) == 21 or sum(player) <= 10 :
            player_card = 11

        elif dealer_card == 1 and sum(dealer) == 21 or sum(dealer) <= 10 :
            dealer_card = 11

        print("player",taken_out_suit_player," player card ",player_card)
        player.append(player_card)


        print(sum(player) ,"\n")

        print("dealer", taken_out_suit_dealer, " dealer card ",dealer_card)
        dealer.append(dealer_card)

        print(sum(dealer),"\n")

    if sum(dealer) >= 21 :
        print("player wins!")
        game_over = True

    elif sum(player) >= 21 :
        print("dealer wins!")
        game_over = True


