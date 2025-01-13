class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and checking balance.
    """

    def __init__(self):
        """
        Initialize the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add a specified amount to the balance.

        Parameters:
        amount (float): The amount to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtract a specified amount from the balance, if sufficient funds are available.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop for user interaction with the checkbook.

    Users can:
    - Deposit money into the checkbook.
    - Withdraw money from the checkbook (if sufficient funds are available).
    - Check the current balance.
    - Exit the program.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            # Exit the program
            print("Exiting. Have a nice day!")
            break
        elif action == 'deposit':
            # Handle deposit action
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            # Handle withdrawal action
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            # Display the current balance
            cb.get_balance()
        else:
            # Handle invalid commands
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

