name = "Lohit"
print(name)

name = "Jethwani"
print(name)

# The thing to note here is that when we run this, by the end of line 5,
# the value of the Variable 'name' has changed to whatever was the last value,
# in this case "Jethwani".

# What this means is that if we wrote a line of code after line 5,
# that uses the Variable name, its going to have the Value of "Jethwani" only.

# Challenge
# Write a program that switches the values stored in the variables a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)