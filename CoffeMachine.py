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

denomination = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

EnoughMoney = True
EnoughResources = True

#MONEY PART

#Calculate the amount the client gave the machine

def Calculate_money_input(quarters, dimes, nickles,pennies):
    total = (denomination["quarters"] * quarters) + (denomination["dimes"] * dimes) + (denomination["nickles"] * nickles) + (denomination["pennies"] * pennies)
    return total

#Calculate if the money is sufficient

def Is_enough(coffe, money):
    cost = MENU[coffe]["cost"]
    change = money - cost
    if change < 0 :
        global EnoughMoney
        EnoughMoney = False
        return print("not enough money")
    else :
        EnoughMoney = True
        return print(f"your change is {change}")

#RESOURCES PART

#Check if the machine has enough resources

def Check_resources(coffe):
    ingredient = MENU[coffe]["ingredients"]
    for ing in ingredient:
        if resources[ing] < ingredient[ing]:
            global EnoughResources
            EnoughResources = False
            return print(f"not enough {ing}")
        else:
            EnoughResources = True
            return 
        
#Make the coffee

def Make_coffee(coffe):
    ingredient = MENU[coffe]["ingredients"]
    for ing in ingredient:
        resources[ing] -= ingredient[ing]
    return print(f"Here is your {coffe}. Enjoy!")


while EnoughResources :
    coffe = input("What would you like? (espresso/latte/cappuccino): ")
    Check_resources(coffe)
    if EnoughResources == False:
        break
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = Calculate_money_input(quarters, dimes, nickles,pennies)
    Is_enough(coffe, money)
    if EnoughMoney == True:
        Make_coffee(coffe)
        
       
   

    




