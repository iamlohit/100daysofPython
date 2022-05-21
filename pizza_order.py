# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BILL = 0
S = 15
M = 20
L = 25

if size == "S":
        BILL = S
elif size == "M":
        BILL = M
elif size == "L":
        BILL = L
if add_pepperoni == "Y":
    if size == "S":
        BILL += 2
    else: 
        BILL += 3
if extra_cheese == "Y":
        BILL += 1
print(f"Your final bill is: ${BILL}")

