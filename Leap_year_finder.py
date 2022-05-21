# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(year % 4)
#print((year % 100) % 2)
#print((year % 400) % 2)

if (year % 4) == 0:
    if ((year % 100) % 2) != 0:
        print("Leap year.")        
    elif ((year % 100) % 2) == 0 and ((year % 400) % 2) == 0:
        print("Leap year.")
else:
    print("Not leap year.")