# When converting Float to Int with the below method, it just chopps off the numbers after Decimal.
print(int(8/3))

# The correct way to do this would be rounding the number.
print(round(8/3))
# 2.66666 gets rounded to 3.

# But how do we control the rouding to a specific number of digits, keeping it a float but simplyfying it.
print(round(8/3,2))
# This gives us 2.67

# A Floor division is similar to converting float to integer by chopping off the numbers after decimal point.
print((8//3))

# We know we cannot print two different data types in the same line without converting one to another.
# Here, we solve it using an f string.
# Everything going within f" " is combined without using '+' signs, any variables go in {} curly braces.
# Cutting down alot of manual labor.
score = 90
isWinning = True
print(f"Your'e score is {score} which is {isWinning}")