from art import logo
import random

def deal_card(deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck.append(random.choice(cards))
    return deck

def calculate_score():
    print()

def compare():
    print()

start = 'y'

while start == 'y':

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    print(logo)

    player_cards = []
    dealer_cards = []

    deal_card(player_cards)
    deal_card(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    print(f"Your  final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")