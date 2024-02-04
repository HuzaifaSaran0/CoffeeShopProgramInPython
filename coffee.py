import time
# TODO 1. All the specs and resources
Menu = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 2,
            "milk": 0
        },
        "cost": 180
    },
    "Latte": {
        "ingredients": {
            "water": 10,
            "milk": 10,
            "coffee": 3
        },
        "cost": 250
    },
    "Cappuccino": {
        "ingredients": {
            "water": 25,
            "milk": 100,
            "coffee": 5
        },
        "cost": 500
    }
}


class Coffee_shop:
    def __init__(self):
        print("////////////////////////////////")
        print("//     SARAN's COFFEE SHOP    //")
        print("////////// Our Menu ////////////\n")
        self.resources = {
            "water": 50,
            "milk": 300,
            "coffee": 100,
            "money": 0
        }
        self.customer_choice = None
        self.quantity = None
        self.decision = None
        self.stay = None

    def services(self):
        for index, name in enumerate(Menu):
            print(f"{index + 1}: {name} (cost: RS.{Menu[name]['cost']})")
        print("\nWhat would You like?")

    def choice(self):
        self.customer_choice = input(":").capitalize()
        self.quantity = int(input("How many Cups?:"))

    def customer_ki_choice(self):
        return self.customer_choice

    def cups(self):
        return self.quantity

    def check_resources(self):
        if self.resources["milk"] >= (Menu[self.customer_choice]["ingredients"]["milk"]) * self.quantity:
            if self.resources["water"] >= (Menu[self.customer_choice]["ingredients"]["water"]) * self.quantity:
                if self.resources["coffee"] >= (Menu[self.customer_choice]["ingredients"]["coffee"]) * self.quantity:
                    self.decision = True

    def insert_money(self):
        money = int(input("Please Insert Money:"))
        time.sleep(1.5)
        self.check_resources()
        amount = Menu[self.customer_choice]["cost"] * self.quantity
        if money >= amount:

            if self.decision:
                change = money - amount
                if change > 0:
                    print(f"Here's your Change of RS.{change}")
                print(f"Take and Enjoy Your delicious {self.customer_choice} coffee")
                self.resources["money"] += amount
                self.resources["milk"] -= (Menu[self.customer_choice]["ingredients"]["milk"]) * self.quantity
                self.resources["water"] -= (Menu[self.customer_choice]["ingredients"]["water"]) * self.quantity
                self.resources["coffee"] -= (Menu[self.customer_choice]["ingredients"]["coffee"]) * self.quantity

            else:
                print("Sorry! We don't have enough resources.")
        else:
            print("Sorry! You don't have enough money for this.")

    def report(self):
        for i in self.resources:
            print(f"{i}: {self.resources[i]}")


stay = True
a = Coffee_shop()


def stay_more():
    global stay
    temp_stay = input("Wanna buy something else??(yes/no):")
    if temp_stay.lower() == "no":
        stay = False
    else:
        stay = True


while stay:
    a.services()
    a.choice()
    a.insert_money()
    time.sleep(1.5)
    stay_more()
