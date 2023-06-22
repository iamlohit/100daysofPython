# Instructions
    # I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
    # https://waitbutwhy.com/2014/05/life-weeks.html
    # Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
    # It will take your current age as the input and output a message with our time left in this format:
    # You have x days, y weeks, and z months left.
    # Where x, y and z are replaced with the actual calculated numbers.
    # Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
    # 56
# Example Output
    # You have 12410 days, 1768 weeks, and 408 months left.

user_age = int(input("What is your current age(in years)? "))

left_years = 90 - user_age
user_days = left_years * 365
user_weeks = left_years * 52
user_months = left_years * 12

print(f"You have {user_days}days, {user_weeks}weeks, and {user_months}months left")