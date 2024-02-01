foodCharge = float(input("Enter the total charge for your meal:\n"))

tip = foodCharge*0.18
tax = foodCharge*0.07

totalCost = foodCharge + tip + tax

print("""The cost of the meal was: ${:.2f}.
The tax on this is ${:.2f}.
The tip amount is: ${:.2f}.
The total cost of the meal with tip and tax is: ${:.2f}.""".format(foodCharge, tip, tax, totalCost))
