#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the TIP Calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill? "))

tip_amt = bill * (1 * tip / 100)
bill_with_tip = bill + tip_amt
amt_per_person = bill_with_tip / people
final_amt = "{:.2f}".format(amt_per_person)
print(f"Each person needs to pay ${final_amt}")