# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2

lower_name = name.lower()

T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")

TRUE = T + R + U + E

L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")

LOVE = L + O + V + E

TRUE_LOVE = (str(TRUE)+str(LOVE))

TRUE_LOVE = int(TRUE_LOVE)

if TRUE_LOVE <= 10 or TRUE_LOVE >= 90:
    print(f"Your score is {TRUE_LOVE}, you go together like coke and mentos.")
elif TRUE_LOVE >= 40 and  TRUE_LOVE <= 50:
    print(f"Your score is {TRUE_LOVE}, you are alright together.")
else:
    print(f"Your score is {TRUE_LOVE}.")