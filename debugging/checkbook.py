class Checkbook:
    def __init__(self):
        """Initialise le solde du compte à 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Dépose une somme d'argent et met à jour le solde."""
        if amount <= 0:
            print("Please enter a valid amount greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Retire une somme d'argent du compte si le solde est suffisant."""
        if amount <= 0:
            print("Please enter a valid amount greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel du compte."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Fonction principale qui gère l'interaction avec l'utilisateur."""
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            print("Goodbye!")
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
