class BankAccount:
    """A SafeBank account with safe deposit and withdraw rules."""

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"{self.owner}: deposit must be positive")
        else:
            self.balance += amount
            print(f"{self.owner}: +INR {amount:,.2f} -> INR {self.balance:,.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.owner}: DENIED, only INR {self.balance:,.2f} available")
        else:
            self.balance -= amount
            print(f"{self.owner}: -INR {amount:,.2f} -> INR {self.balance:,.2f}")

acct = BankAccount("Priya Sharma", 5000)
acct.deposit(3000)
acct.withdraw(10000)
acct.withdraw(6500)