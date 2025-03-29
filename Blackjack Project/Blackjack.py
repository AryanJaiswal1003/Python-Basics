#Blackjack Project
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score , c_score):
    if u_score == c_score:
        return "Draw!!!😫😌"
    elif c_score == 0:
        return "Opponent Scores a Blackjack. You Loose!!!😉😝"
    elif u_score == 0:
        return "User Scores a Blackjack. You Win!!!🥲🫡"
    elif u_score > 21:
        return "You Went Over. You Loose!!!🤪😌"
    elif c_score > 21:
        return "Opponent Went Over. You Win!!!🤦‍♂️😅"
    elif u_score > c_score:
        return "You Win!!!😝🫡"
    else:
        return "You Loose!!!🤣😌"

def game_continue():
    from art import logo
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    computer_score = -1
    user_score = -1
    for char in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'Y' to get Another Card, Type 'N' to Pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(u_score=user_score , c_score=computer_score))

while input("Do you want to Play a Game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
    print("\n" * 20)
    game_continue()