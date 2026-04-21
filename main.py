# Ingredients and cost in a dictionary
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

# initial resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0   # initialise money 
# Global variables
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

def resource_sufficient(choice):
    """Checks if there is enough resources to make your drink."""
    for ingredient in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def subtract_resource(choice):
    """Reduces the ingredients once a drink is made."""
    for ingredient in MENU[choice]['ingredients']:
        resources[ingredient] -= MENU[choice]['ingredients'][ingredient]

def report_resource():
    """Gives you information on the ingredients and money left."""
    for element in resources:
        if element == 'coffee':
            unit = "g"
        else:
            unit = "ml"
        print(f"{element.capitalize()}: {resources[element]}{unit}")
    print(f"Money: ${money}")

def total_coin_amount():
    "Calculates the amount user feeds the machine."
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return QUARTER*quarters + DIME*dimes + NICKEL*nickels + PENNY*pennies

continue_game = True
while continue_game:
    # Gets user choice on repeat
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        print("Powering off!")
        continue_game = False   # This is your cue to get out

    elif user_choice == "report":
        report_resource()

    else:
        # Check if resource is sufficient
        if not resource_sufficient(user_choice):
            continue

        subtract_resource(user_choice)      # Subtract resources
        total_coins = total_coin_amount()   # Get money

        if total_coins < MENU[user_choice]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total_coins > MENU[user_choice]['cost']:
            print(f"Here is ${round(total_coins - MENU[user_choice]['cost'], 2)} dollars in change.") # round(a,2) coz 2 decimal points is enough

        money += MENU[user_choice]['cost']              # updating money
        print(f"Here is your {user_choice}. Enjoy!;)")