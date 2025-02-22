class CoffeeMachine:
    def __init__(self,menu,transaction):
        self.menu = menu
        self.transaction = transaction
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def is_resource_sufficient(self,order_ingredients):
        for ingredient in order_ingredients:
                if self.resources[ingredient] < order_ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    return False
        return True
    
    def make_coffee(self,drink_name,order_ingredients):
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")
    
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ₹{self.transaction.profit}")