print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill with? "))

tip_percent /= 100
tip_amt = (total_bill * tip_percent)
amt_with_tip = total_bill + tip_amt
final_amt = round(amt_with_tip / people, 2)

print(f"Each person should pay: ${final_amt}")