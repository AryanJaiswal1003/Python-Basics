#link = https://appbrewery.github.io/python-day14-demo/

#TODO-1: Generate Random data and Compare it with other data
from art import logo , vs
from gamedata import data

# change = []
# for char in data:
#     change.append(char['name'])
# print(change)

def compare():
    game_over = False
    number = 0
    while not game_over:
        Name = data[number]['name']
        Description = data[number]['description']
        Country = data[number]['country']
        print(f"Compare A: {Name}, a {Description}, from {Country}")
        number += 2
        if number == 50:
            game_over = True
        else:
            continue

def against():
    game_over = False
    number = 1
    while not game_over:
        Name = data[number]['name']
        Description = data[number]['description']
        Country = data[number]['country']
        print(f"Against B: {Name}, a {Description}, from {Country}")
        number += 2
        if number == 51:
            game_over = True
        else:
            continue

compare()
against()