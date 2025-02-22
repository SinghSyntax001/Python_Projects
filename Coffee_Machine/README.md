
# ☕ Coffee Machine Simulator

A simple Coffee Machine simulation in Python that allows users to order coffee, process payments, and manage resources. The program supports multiple coffee types and ensures resource availability before making a drink.

## 🛠 Features
- Choose from **Espresso, Latte, and Cappuccino**.
- Checks if resources (water, milk, coffee) are sufficient before preparing the drink.
- Handles **payment transactions** with Indian currency notes.
- Provides a **report** of available resources and earnings.
- Allows the user to **exit** at any time.

## 📂 Project Structure
```plaintext
📦 CoffeeMachine-Simulator
│── CoffeeMachine.py   # Handles coffee preparation and resource management
│── Menu.py            # Stores coffee menu details (ingredients & prices)
│── Transaction.py     # Manages payment processing and profit tracking
│── Main.py            # Main script to run the Coffee Machine program
```

## 🚀 How to Run
1. **Clone the repository**  
   ```sh
   git clone https://github.com/SinghSyntax001/Coffee_Machine.git
   cd Coffee_Machine
   ```
2. **Run the program**  
   ```sh
   python Main.py
   ```
3. **Follow on-screen instructions** to order coffee.

## 💰 Payment System
- The machine accepts **₹500, ₹200, ₹100, ₹50, ₹20, ₹10** notes.
- If insufficient money is inserted, the transaction is canceled.
- If excess money is inserted, **change is returned**.

## 📊 Resource Management
- The machine keeps track of **water, milk, and coffee levels**.
- Use the command **"report"** to check available resources and total earnings.

## 📝 Example Usage
```plaintext
What would you like? (espresso/latte/cappuccino) or (exit): latte
100 rupees for latte.
Please insert notes. Enter each note value one by one, type 'done' when finished.
Insert note (₹500, ₹200, ₹100, ₹50, ₹20, ₹10) or type 'done': 100
Here is your latte. Enjoy!
```

## 🏆 Future Enhancements
- Add more coffee options.
- Implement a GUI using Tkinter or PyQt.
- Enhance payment handling for digital transactions.

## 📜 License
This project is open-source. Feel free to modify and contribute!

---
Made with ❤️ by [Shashank Singh] https://github.com/SinghSyntax001)

