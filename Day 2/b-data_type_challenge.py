# Instructions
    # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

    # Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input
    # 39

# Example Output
    # 3 + 9 = 12
    # 12


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number))

# Since we never told the Input function to store the Input User Data as Integer, it defaults to a String.

# We can do it the long way, more readable:

    # Subscripting the User Input String Value and assining it to Variables.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

    # Typecasting from str to int
first_digit = int(first_digit)
second_digit = int(second_digit)

    # Adding the sum of the two values, saving it in a new Variable called result.
    # NOTE: If we did not first convert the Strings to Integers, instead of Mathematical SUM (+) it would be a String Concatenation.
result = first_digit + second_digit

    # Printing the Result
print(result)

# OR We could do this simply in one line as follows:
print(int(two_digit_number[0]) + int(two_digit_number[1]))