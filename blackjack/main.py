############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = []
    card.append(random.choice(cards))
    card.append(random.choice(cards))
    return card

def deal_another_card(current_hand):
    card = current_hand
    card.append(random.choice(cards))
    return card

def deal_computer_card(current_hand):
    card = current_hand
    if sum(card) < 16:
        card.append(random.choice(cards))
        return card
    else:
        return card

def show_result(players_hand, computers_hand):
    print(f"Your final hand: {players_hand}")
    print(f"Computer's final hand: {computers_hand}")
    if sum(players_hand) > 21:
        print("You lose")
    elif sum(players_hand) > sum(computers_hand):
        print("You win")
    elif sum(players_hand) == sum(computers_hand):
        print("Tie")
    else:
        print("You lose")

def blackjack():
    players_card = deal_card()
    computers_card = deal_card()
    print(f"Your cards: {players_card}")
    print(f"Computer's first card: {computers_card[0]}")
    should_continue = True
    while should_continue:
        cont = input("Type 'y' to get another card, type 'n' to pass: ")
        if cont == 'y':
            new_players_card = deal_another_card(players_card)
            if sum(new_players_card) > 21:
                new_computers_card = deal_computer_card(computers_card)
                show_result(new_players_card, new_computers_card)
                should_continue = False
                if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
                    blackjack()
            elif sum(new_players_card) <= 21:
                print(f"Your cards: {new_players_card}")
                should_continue = True
        else:
            new_computers_card = deal_computer_card(computers_card)
            show_result(players_card, new_computers_card)
            should_continue = False
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
                blackjack()

blackjack()

