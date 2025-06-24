# is it something stupid
import random
def blackjack():
    cards = {
            "heart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
            "club": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
            "spade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
            "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        }


    def player(cards):
        # if in the dict there is no card left at certain key then we too look out thaat part from the dict
        available_cards = [suit for suit in cards.keys() if len(cards[suit]) >= 2]

        if len(available_cards) < 2 :
            print("No more cards! Game over.")

        suit = random.choice(available_cards)

        card = random.choice(cards[suit])
        # now we have to remove that card from the deck
        cards[suit].remove(card)
        return card, suit


    def dealer(cards):
        # if in the dict there is no card left at certain key then we too look out thaat part from the dict
        available_cards = [suit for suit in cards.keys() if len(cards[suit]) >= 2]

        if len(available_cards) < 2:
            print("No more cards! Game over.")
            return None, None

        suit = random.choice(available_cards)

        card = random.choice(cards[suit])
        # now we have to remove that card from the deck
        cards[suit].remove(card)
        return card, suit


    players_hand = []
    dealer_hand = []


    for _ in range(2):
        card_dealer, suits_dealer = dealer(cards)
        card_player, suits_player = player(cards)

        players_hand.append(card_player)
        dealer_hand.append(card_dealer)

    print("Players hand:", players_hand)
    print("Dealer hand:", dealer_hand[0])

    print("Player's score:", sum(players_hand))

    while True:
        hit = input("do you wanna hit or stand ? hit or stand: ").lower()
        score_player = sum(players_hand)
        if score_player > 21:
            print("you lose! Computer wins")
            break

        if hit == "hit":
            players_hand.append(player(cards)[0])
            print("your other card :", players_hand)
            score_player = sum(players_hand)
            print("score ", score_player)


        elif hit == "stand":
            break

        else:
            print("hit or stand")


    # dealer turn
    print("\nDealer's hand:", dealer_hand)

    while sum(dealer_hand) <17:

        dealer_hand.append(dealer(cards)[0])

    score_dealer = sum(dealer_hand)
    score_player = sum(players_hand)

    if score_dealer > 21 or score_player > score_dealer:
        print("you win! Computer lose")

    elif score_dealer > score_player:
        print("you lose! Computer wins")
    else:
        print("its a tie")



prompt = input("do you wanna play the game yes or no? ")
if prompt == "yes":
    blackjack()

else:
    print("Game over.")