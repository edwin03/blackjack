from art import logo
import random

def deal_card(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck.append(random.choice(cards))
    return deck

def calculate_score(cards):
    total = sum(cards)
    if total > 21 and 11 in cards:
        total -= 10
    return total

def compare(p_total, d_total):
    if p_total == 21 and d_total == 21:
        print("Is a tie!")
    elif p_total == 21:
        print("You win!")
    elif d_total == 21:
        print("You lose!") 
    elif p_total > 21:
        print("You lose!")
    elif d_total > 21:
        print("You win!")
    elif p_total > d_total:
        print("You win!")
    else:
        print("You lose!")

start = 'y'

while start == 'y':

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    print(logo)

    player_cards = []
    dealer_cards = []

    deal_card(player_cards)
    deal_card(player_cards)
    deal_card(dealer_cards)

    draw = "y"

    while draw == 'y':
        print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw == 'y':
            deal_card(player_cards)

    print(f"Your  final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
    compare(calculate_score(player_cards), calculate_score(dealer_cards))