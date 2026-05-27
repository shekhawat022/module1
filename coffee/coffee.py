class Coffee:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def brew(self):
        print("\nMaking", self.name)
        print("Ingredients:")
        
        for item in self.ingredients:
            print("-", item)


latte = Coffee("Latte", ["Espresso", "Milk", "Foam"])
americano = Coffee("Americano", ["Espresso", "Hot Water"])
matcha = Coffee("Matcha Latte", ["Matcha Powder", "Milk"])
cappuccino = Coffee("Cappuccino", ["Espresso", "Milk Foam"])
espresso = Coffee("Espresso", ["Coffee", "Water"])


while True:
    print("\n--- COFFEE MENU ---")
    print("1. Latte")
    print("2. Americano")
    print("3. Matcha Latte")
    print("4. Cappuccino")
    print("5. Espresso")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        latte.brew()

    elif choice == "2":
        americano.brew()

    elif choice == "3":
        matcha.brew()

    elif choice == "4":
        cappuccino.brew()

    elif choice == "5":
        espresso.brew()

    elif choice == "q":
        print("Thank you!")
        break

    else:
        print("Invalid choice")