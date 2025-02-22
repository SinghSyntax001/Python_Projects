from Menu import Menu
from Transaction import Transaction
from CoffeeMachine import CoffeeMachine

class Main:
    def __init__(self):
        self.menu = Menu()
        self.transaction = Transaction()
        self.coffee_machine = CoffeeMachine(self.menu, self.transaction)
        self.is_on = True
    
    def run(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino)or(exit): ")
            if choice == "exit":
                self.is_on = False
            elif choice == "report":
                self.coffee_machine.report()
            else:
                drink = self.menu.get_item(choice)
                if drink and self.coffee_machine.is_resource_sufficient(drink["ingredients"]):
                    payment = self.transaction.process_payment(choice, drink["cost"])
                    if self.transaction.is_transaction_successful(payment, drink["cost"]):
                        self.coffee_machine.make_coffee(choice, drink["ingredients"])
                else:
                    print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_program = Main()
    main_program.run()