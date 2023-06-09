from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bidder_dict = {}
end_of_auction = False

def blind_auction(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while not end_of_auction:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidder_dict[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n").lower()
    if should_continue == "no":
        end_of_auction == True
        blind_auction(bidder_dict)
        print(bidder_dict)
    elif should_continue == "yes":
        clear()
