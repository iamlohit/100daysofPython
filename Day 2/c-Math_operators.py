# Addition
print(3 + 5)

# Subtraction
print(5 - 3)

# Multiplication
print(5 * 5)

# Division
print (25 / 5)
# NOTE: When ever we devide two integers, the answer/result is always a Float Type number.

# Exponent - Raise number to a power
print(4**4)

# What if we have multiple calculations on the same line, which happens first ? :)

# PEMDAS
    # () - Inner most bracket or Parenthesis is calculated first, regardless.
    # **
    # * & /
    # + & -

# Eg: What would be result of following:
print(3 * 3 + 3 / 3 - 3)
    # Everything is one bracket, check.
    # No Exponent used, check.
    # Multiplication should happen first, so now its (9 + 3 / 3 - 3)
    # Division happens next, so now its (9 + 1 - 3)
    # Addition should happen first, so now its (10 - 3)
    # Subtraction happens last, so result SHOULD be (7)
    # NOTE: Data Type should be Float since we used "/", so ANS = 7.0

# Eg: How Bracket changes things:
print(3 * (3 + 3) / 3 - 3)
    # Parenthesis calculation happens first, so now its (3 * 6 / 3 - 3)
    # No Exponent used, check.
    # Multiplication happens first, so now its (18 / 3 - 3)
    # Division comes next, so now its (6 - 3)
    # No Addition used, check.
    # Subtraction happens last, so result should be (3.0)