# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
bid_game = {}
bid_process = True

#TODO-4(1): Comparing Bids in Dictionary [MY WAY]
while bid_process:
    key = input("What is Your Name? = ")
    value = int(input("What is the Bid Amount? = Rs. "))
    bid_game[key] = value
    bid = input("Are there any other Bidders: TYPE 'YES' or 'NO'.\n").lower()

    if bid == "no":
        bid_process = False
    elif bid == "yes":
        print("\n" * 100)
    else:
        bid_process = False
        print("You Entered a Wrong Input.. Start Again.. Thankyou")

max_value = 0
max_key = ""
for key, value in bid_game.items():
    if value > max_value:
        max_key = key
        max_value = value
print(f"The Winner is {max_key} with Bid of Rs. {max_value}")

#TODO-4(2): Comparing Bids in Dictionary [TEACHER WAY]
def find_highest_bidder(bid_dic):
    winner = ""
    highest_bid = 0
    for bidder in bid_dic:
        bid_amount = bid_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The Winner is {winner} with Bid of Rs. {highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    key = input("What is Your Name? = ")
    value = int(input("What is the Bid Amount? = Rs. "))
    bids[key] = value
    bid = input("Are there any other Bidders: TYPE 'YES' or 'NO'.\n").lower()
    if bid == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif bid == "yes":
        print("\n" * 100)