MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    global resources
    Water = resources["water"]
    Milk = resources["milk"]
    Coffee = resources["coffee"]
    global profit
    print(f"Water: {Water}ml")
    print(f"Milk: {Milk}ml")
    print(f"Coffee: {Coffee}g")
    print(f"Profit: ${profit}")

def check_resources(coffee):
        global resources
        Water = resources["water"]
        Milk = resources["milk"]
        Coffee = resources["coffee"]
        if MENU[coffee]["ingredients"]["water"] <= Water:
            if "milk" not in MENU[coffee]["ingredients"]:
                return True
            if 'milk' in MENU[coffee]["ingredients"] and MENU[coffee]["ingredients"]['milk'] <= Milk:
                if MENU[coffee]["ingredients"]["coffee"] <= Coffee:
                    return True
                else:
                    print("Sorry, there is not enough coffee.")
                    return False
            else:
                print(f"Sorry there is not enough milk.")
                return False
        else:
            print(f"Sorry there is not enough water.")
            return False

def inventory_reducer(menu_item_reciepe):
    global resources
    resources["water"] -= MENU[menu_item_reciepe]["ingredients"]["water"]
    if 'milk' in MENU[menu_item_reciepe]["ingredients"]:
        resources["milk"] -= MENU[menu_item_reciepe]["ingredients"]['milk']
    resources["coffee"] -= MENU[menu_item_reciepe]["ingredients"]["coffee"]

def collect_coins(menu_item_cost):
    global profit
    quarter = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01
    print("Please insert coins:")
    given_quarters = int(input("Quarters: "))
    given_dimes = int(input("Dimes: "))
    given_nickles = int(input("Nickles: "))
    given_pennies = int(input("Pennies: "))
    total_value = (given_quarters * quarter) + (given_nickles * nickles) + (given_dimes * dimes) + (given_pennies * pennies)
    if total_value > menu_item_cost:
        change = round(total_value - menu_item_cost)
        profit += menu_item_cost
        print("Here is your coffee ☕️ , enjoy! ")
        print(f"Here is your change: ${change}")
    elif total_value == menu_item_cost:
        profit += menu_item_cost
        print("Here is your coffee ☕️ , enjoy! ")
    elif total_value < menu_item_cost:
        print("Sorry that's not enough money. Money refunded.")

is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print_report()
    elif user_choice == "off":
        is_on = False
        continue
    else:
        if check_resources(user_choice) and user_choice != "report":
            # user_key = '"' + user_choice + '"'
            cost = int(MENU[user_choice]["cost"])
            collect_coins(cost)
            inventory_reducer(user_choice)
