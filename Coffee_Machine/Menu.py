class Menu:
    def __init__(self):
        self.items = {
            "espresso": {"ingredients": {"water": 50, "coffee": 10}, "cost": 150},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 100},
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 80},
        }
    
    def get_item(self, name):
        return self.items.get(name, None)