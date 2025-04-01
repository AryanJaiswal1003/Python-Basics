from art import logo , vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and return the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess , a_followers , b_followers):
    """Take a user's guess and tell follower counts and return if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:
    #Generate a random account from the game data

    #Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if the user is correct
    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess , a_follower_count , b_follower_count)

    #Give user feedback on their guess
    #Score Keeping
    if is_correct:
        score += 1
        print(f"You're Right! Current Score {score}")
    else:
        print(f"Sorry you are Wrong. Final Score {score}")
        game_continue = False