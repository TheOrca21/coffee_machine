import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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



def avail(order, resources):
    req = order['ingredients']
    resources['water'] -= req['water']
    resources['milk'] -= req['milk']
    resources['coffee'] -= req['coffee']
    return resources


def find_order(MENU):
    choice = input("what would you like(espresso/latte/cappuccino): ")
    if choice in MENU:
        item = MENU[choice]
        return item
    elif choice == 'off':
        print("Goodbye dear friend☹️")
        sys.exit()
    elif choice == 'report':
        print(f"water,milk,coffee left:{resources}ml")
        find_order(MENU)
    else:
        print('Invalid option restarting...')
        find_order(MENU)


def cost_calc(order):
    ic = order['cost']
    penny = int(input("How many pennies?:"))
    nickel = int(input("How many nickels?:"))
    dime = int(input("How man dimes?:"))
    quarters = int(input("How many quarters?:"))
    am = (penny*0.01)+(nickel*0.05)+(dime*0.10)+(quarters*0.25)
    total = am-ic
    return total

on = True
while on:
    order = find_order(MENU)
    val = avail(order, resources)
    if val['water'] <= 0 or val['milk'] <= 0 or val['coffee'] <= 0:
        print("Sorry we are out of resources!! 😢 ")
        print("Refill and restart to enjoy!")
        on = False
    else:
        amount = cost_calc(order)
        if amount >= 0:
            print(f"You're order is being prepared meanwhile here is your change {amount}$ ")
            print("Here's your order enjoy☕")
        else:
            print("not enough money😖")
            print("please try again")
            on = False
