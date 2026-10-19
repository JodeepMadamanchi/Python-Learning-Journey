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
money = 0
game_over = False
while not game_over:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":
        game_over = True
        continue

    if coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        continue

    if coffee_type == "money":
        print(money)
        continue

    for item in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            break
    else:
        print("PLEASE INSERT COINS HERE")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)



        if total_money >= MENU[coffee_type]["cost"]:
            print(f'Here is {round(total_money - MENU[coffee_type]["cost"], 2)} in change.')
            print(f"Here is your {coffee_type} ☕️. Enjoy!")
            game_over = False
            money += MENU[coffee_type]["cost"]
            for item in MENU[coffee_type]["ingredients"]:
                resources[item] -= MENU[coffee_type]["ingredients"][item]


        elif total_money < MENU[coffee_type]["cost"]:
            print(f"Sorry that's not enough money. Money refunded.")
            game_over = False
