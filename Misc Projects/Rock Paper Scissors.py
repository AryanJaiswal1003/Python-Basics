rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
'''

game = [rock , paper, scissors]
user_input = int(input("Type your choice: '0' for Rock , '1' for Paper or '2' for Scissors.\n"))
if user_input >= 0 and user_input <= 2:
    print(game[user_input])
import random
computer = random.randint(0 , 2)
print("Computer chose:\n" + game[computer])
if user_input > 2 or user_input < 0:
    print("You entered a Wrong Input. You loose!!")
elif user_input == 0 and computer == 2:
    print("You Win!!")
elif user_input == 2 and computer == 0:
    print("You Loose!!")
elif user_input > computer:
    print("You Win!!")
elif user_input < computer:
    print("You Loose!!")
elif user_input == computer:
    print("Game Draw!!")