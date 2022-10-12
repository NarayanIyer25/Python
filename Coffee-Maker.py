menu = {
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






def process_coins(q, d, n, p):
    quarter = 0.25 * q
    dimes = 0.10 * d
    nickles = 0.05 * n
    pennies = 0.01 * p
    return quarter + dimes + nickles + pennies


game_on = True
while game_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        game_on = False
    elif user_input == 'report':
        print("water :" ,  resources['water'])
        print("milk: ", resources['milk'])
        print("coffee: ", resources['coffee'])
    else:
        if user_input == 'espresso'  and (resources['water']>=menu[user_input]['ingredients']['water']) and (resources['coffee']>=menu[user_input]['ingredients']['coffee']):
            q = int(input("enter quarter: "))
            d = int(input("enter dimes: "))
            n = int(input("enter nickel: "))
            p = int(input("enter pennies: "))
            total = process_coins(q, d, p, n)
            if total > menu[user_input]['cost']:
                change = round(total, 2) - menu[user_input]['cost']
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {user_input}. Enjoy!”")
            else:
                print("Sorry that's not enough money. Money refunded.")
            resources['water'] = resources['water'] - menu[user_input]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - menu[user_input]['ingredients']['coffee']
        elif (resources['water'] >= menu[user_input]['ingredients']['water']) and (
                resources['coffee'] >= menu[user_input]['ingredients']['coffee']) and (
                resources['milk'] >= menu[user_input]['ingredients']['milk']):
            q = int(input("enter quarter: "))
            d = int(input("enter dimes: "))
            n = int(input("enter nickel: "))
            p = int(input("enter pennies: "))
            total = process_coins(q, d, p, n)
            if total > menu[user_input]['cost']:
                change = round(total, 2) - menu[user_input]['cost']
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {user_input}. Enjoy!”")
            else:
                print("Sorry that's not enough money. Money refunded.")
            resources['water'] = resources['water'] - menu[user_input]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - menu[user_input]['ingredients']['coffee']
            resources['milk'] = resources['milk'] - menu[user_input]['ingredients']['milk']
        else:
            if resources['water'] < menu[user_input]['ingredients']['water']:
                print("insufficient Water")
            elif resources['coffee'] < menu[user_input]['ingredients']['coffee']:
                print("insufficient coffee")
            elif user_input != 'espresso' and resources['milk'] < menu[user_input]['ingredients']['milk']:
                print("insufficient milk")


