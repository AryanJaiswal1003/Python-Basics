import random

a = 0
def guess_number():
    global a
    from art import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    a = random.randint(1 , 100)
    print(f"I'm Thinking of a Number between 1 and 100. {a}")

def game(lives):
    while not lives == 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_choice = int(input("Make a Choice = "))
        if user_choice > a:
            lives -= 1
            print("Too High!!!\nGuess Again!!!")
        elif user_choice < a:
            lives -= 1
            print("Too Low!!!\nGuess Again!!!")
        elif user_choice == a:
            print("*************** You Win!!! ****************")
            print("\n" * 2)
            break

        if lives == 0:
            print("********** You Run out of Guesses!!! ************")
            print("\n")
            print(f"******* You Loose!!! The Correct Number is = {a} **********")


def game_continue():
    guess_number()
    choice = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()

    if choice == "easy":
        game(lives=10)
    elif choice == "hard":
        game(lives=5)
    else:
        print("\n")
        print("You Entered a Wrong Input. Please Try Again by Refreshing the Game!!")
        print("\n" * 3)

while input("Do you want to Play the Number Game? Type 'Y' or 'N': ").lower() == "y":
    print("\n" * 30)
    game_continue()