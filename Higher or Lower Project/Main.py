#link = https://appbrewery.github.io/python-day14-demo/

#TODO-1: Generate Random data and Compare it with other data
from game_data import data
from art import logo , vs
import random


def assertion(num):
    user = data[num]['name']
    user_description = data[num]['description']
    user_country = data[num]['country']
    return f"Compare A: {user}, a {user_description}, from {user_country}"


def against(num):
    print(vs)
    user = data[num]['name']
    user_description = data[num]['description']
    user_country = data[num]['country']
    return f"Against B: {user}, a {user_description}, from {user_country}"


index1 = random.randrange(0 , 50)
game_over = False
user_score = 0

while not game_over:
    index2 = random.randrange(0, 50)
    a = data[index1]['follower_count']
    b = data[index2]['follower_count']

    print(logo)
    if user_score > 0:
        print(f"You're Right! Current Score: {user_score}")

    print(assertion(num=index1))
    print(against(num=index2))

    user_input = input("Who has More Followers? Type 'A' or 'B' = ").lower()
    print("\n" * 20)

    if user_input == "a" and a > b:
        index1 = index2
        user_score += 1
        continue
    if user_input == "b" and b > a:
        index1 = index2
        user_score += 1
        continue
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {user_score}")
        break