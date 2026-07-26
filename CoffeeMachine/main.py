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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

initial_report = {}
profits = 0


def drink_ingredient(drink_type):
    if drink_type in MENU:
        drink_mix = MENU[drink_type]["ingredients"]
        drink_cost = MENU[drink_type]["cost"]
        return drink_mix, drink_cost
    return None, "Item not found"


def resources_sufficiency(drink_resources):
    global initial_report

    new_report = {}
    if not initial_report:
        initial_report = resources.copy()

    for item in drink_resources:
        if drink_resources[item] > initial_report[item]:
            print(f"Available resources: {initial_report}\n Resources needed: {drink_resources}")
            return False, f"Sorry there's not enough {item}"

        new_report[item] = initial_report[item] - drink_resources[item]

    return True, (initial_report, new_report)


def get_valid_coin(prompt, value):
    while True:
        try:
            return int(input(prompt)) * value
        except ValueError:
            print("Sorry, please insert an integer.")


def coin_evaluator(drink_price):
    print("Please insert coins.")
    total = 0
    while total < drink_price:
        total += get_valid_coin("how many quarters?: ", 0.25)
        if total >= drink_price:
            break
        total += get_valid_coin("how many dimes?: ", 0.1)
        if total >= drink_price:
            break
        total += get_valid_coin("how many nickels?: ", 0.05)
        if total >= drink_price:
            break
        total += get_valid_coin("how many pennies?: ", 0.01)
        if total >= drink_price:
            break
        return False

    return total


def coffee_machine():
    global initial_report
    global profits

    print("For maintenance, report or profit enter: 'off', 'report' or 'profit' accordingly")
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_drink == "report":
        if not initial_report:
            initial_report = resources.copy()
        print(f"Available Resources: {initial_report}")
        return False
    elif user_drink == "profit":
        print(f"${profits}")
        return False
    elif user_drink == "off":
        return False


    drink_mix, drink_cost = drink_ingredient(user_drink)

    """Unpack the boolean success flag and the data payload"""
    success, data = resources_sufficiency(drink_mix)

    if not success:
        print(data)
        return False

    """Safely unpack my dictionary ONLY if successful"""
    initial_report, new_report = data

    money_entered = coin_evaluator(drink_cost)

    if money_entered >= drink_cost:
        profits += drink_cost
        print(f"Processing {user_drink}")
        if money_entered > drink_cost:
            change = round(money_entered - drink_cost, 2)
            print(f"Take your change: ${change}")
    else:
        print(f"Sorry, not enough funds, {user_drink} cost ${drink_cost}. Refunding your money ${round(money_entered, 2)}")
        return False

    # print(f"Report before purchasing {user_drink}: {initial_report}")
    # print(f"Report after purchasing {user_drink}: {new_report}")
    print(f"Here is your {user_drink}. Enjoy!")

    initial_report = new_report
    return True


while True:
    coffee_machine()
    buy_drink = input("Want to buy drink (yes/no): ").lower()

    if buy_drink == "yes":
        continue
    else:
        break