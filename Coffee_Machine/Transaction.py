class Transaction:
    def __init__(self):
        self.profit = 0
    
    def process_payment(self, drink_name, drink_cost):
        print(f"{drink_cost} rupees for {drink_name}.")
        print("Please insert notes. Enter each note value one by one, type 'done' when finished.")
        
        accepted_notes = [500, 200, 100, 50, 20, 10]
        total = 0
        while True:
            note = input("Insert note (₹500, ₹200, ₹100, ₹50, ₹20, ₹10) or type 'done': ")
            if note.lower() == "done":
                break
            try:
                note = int(note)
                if note in accepted_notes:
                    total += note
                else:
                    print("Invalid note. Please insert valid currency.")
            except ValueError:
                print("Invalid input. Please enter a valid note value.")
        return total
    
    def is_transaction_successful(self, money_received, drink_cost):
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ₹{change} in change.")
            self.profit += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False