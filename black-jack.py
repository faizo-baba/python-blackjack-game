import random as r
import os
import art


def deal_card():
    """this function pick a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return r.choice(cards)

def calculation(cards):
    """this function add the cards and print the 
    total score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """this function compare both computer score and user score
    and show the winner"""
    if user_score == computer_score:
        return "Draw! You should play another game."
    elif computer_score == 0:
        return "Lose! Opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "Lose! You went over 21."
    elif computer_score > 21:
        return "You win! Opponent went over 21."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."
    
def play_game ():
    print( art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculation(user_cards)
        computer_score = calculation(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'yes' to get another card, type 'no' to pass: ")
            if another_card.lower() == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards until it reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculation(computer_cards)

    


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("want to play a game of BLACKJACK YES/NO: ") == "yes" :
    os.system("clear")
    play_game()
