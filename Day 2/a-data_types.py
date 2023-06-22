# Data Types

# Strings 
    # - This contains letters A-Z, a-z
    # NOTE: Anthing within " " becomes a string, so "123" is a string, NOT a number.
    # Each item is indexed starting with 0 in a string
    # Pulling out or Disecting an element from a string is called - Subscripting

print("Hello"[0])

# Integer
    # Whole Numbers without Decimals
    # Numbers can contain _ like 123_456_789 - but they will be read by computer as a single number.
    # This is just done for human readability.

print(123 + 345)

# Float
    # Numbers with Decimals

3.14159

# Boolean
    # Only has 1 of 2 values.
    # Always has first letter Capital
    # Is NEVER used with "TRUE" / "FALSE" QUOTES.

True
False

# How to check which data type you are using ?
    # Introducing the type() check function

type("Hello")
type(123)
type(123.456)
type(True)

# We can also do Type Conversion - or Type Casting

num = str(123)
type(num)

num = float(123)
type(num)

print(str(70) + str(100))
# Prints 70100

print(70 + float("100.5"))
# Prints 170.5
    # Inner most bracet function is done first.


