# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Max_age = int(90)
Current_age = int(Max_age) - int(age)

Days_Left = Current_age * 365
Weeks_left = Current_age * 52
Months_left = Current_age * 12

print(f"You have {Days_Left} days, {Weeks_left} weeks, and {Months_left} months left")