from menu import MENU
from resources import resources



def report():
    print(f" Water: {resources['water']}")
    print(f" Milk: {resources['milk']}")
    print(f" Coffee: {resources['coffee']}")
    print(f" Money: {resources['money']} ")


def total_money_given(quarters, dimes, nickles, penny):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_penny = penny * 0.01
    total = total_quarters + total_dimes + total_nickles + total_penny

    return total


def calculate_cost(drink, money_recieved):
    change = money_recieved - MENU[drink]['cost']
    resources['money'] = resources['money'] + MENU[drink]['cost']
    return round(change, 2)



def deduct_resources(drink):
        ingredients = MENU[drink]['ingredients']
        for resource in ["coffee", "milk", "water"]:
            ingredient = ingredients.get(resource, 0)
            if resources[resource] < ingredient:
                raise ValueError(f"Not enough {resource}!")
            resources[resource] -= ingredient


def main():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == 'report':
            report()
            break
        if user_choice == 'off':
            quit()
        print("Please insert coins.")
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        penny = float(input("how many penny's?: "))
        money_recieved = total_money_given(quarters, dimes, nickles, penny)
        if money_recieved < MENU[user_choice]['cost']:
            print("You don't have enough money!")
            break



        change = calculate_cost(user_choice, money_recieved )
        print(change)
        deduct_resources(user_choice)
        print(f"Enjoy your {user_choice} :) ")
        if change > 0:
            print(f"Here is ${change} dollars in change")




main()
