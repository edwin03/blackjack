from art import logo
import random, os

def deal_card(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck.append(random.choice(cards))
    return deck

def calculate_score(cards):
    total = sum(cards)
    if total > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return total

def compare(p_total, d_total):
    if p_total == d_total:
        print("Is a tie!")
    elif p_total == 21:
        print("You win!")
    elif d_total == 21:
        print("You lose!")
    elif p_total > 21:
        print("You went over! You lose!")
    elif d_total > 21:
        print("Dealer went over! You win!")
    else:
        if p_total > d_total:
            print("You win!")
        else:
            print("You lose!")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

start = 'y'

while start == 'y':

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    clear_screen()

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
        if calculate_score(player_cards) > 21:
            draw = 'n'
        if calculate_score(dealer_cards) < 17:
            deal_card(dealer_cards)

    print(f"Your  final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
   
    compare(calculate_score(player_cards), calculate_score(dealer_cards))