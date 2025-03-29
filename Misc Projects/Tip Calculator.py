#Calculator Project
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill: Rs. "))
taxing = int(input("Tax%: "))
tip = int(input("How much tip would you like to give us [0, 10, 12 or 15]%: "))
other_cost = int(input("Delivery & Shipping Cost: Rs. "))
people = int(input("How many people to split the bill: "))
offer = 100
Bill_post_Taxing = bill + ((taxing / 100) * bill)
Bill_post_Tip = Bill_post_Taxing + ((tip / 100) * bill)
Bill_post_Misc_costs = Bill_post_Tip + other_cost
print("Discount Applied [Offer100]: Rs. 100")
Bill_post_offer = Bill_post_Misc_costs - offer
Final_Bill = Bill_post_offer / people
Final_divided_bill = round(Final_Bill , 2)

print(f"Each Person should Pay: Rs. {Final_divided_bill}")