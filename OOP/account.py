
# Encapsulation - It is used to protect or hide the internal details of a class and provides access to the data and methods through an interface.
# Private methods and attributes are prefixed with an underscore

class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.__overdraft_limit = 0
        self.__minimum_balance = 0
        self.__is_frozen = False
        self.__transaction_history = [] 


        
    def check_balance(self, pin):
        if (pin == self.__pin):
            return self.__balance
        
        else: 
            return "wrong pin"
       

    def deposit(self, amount):
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: {amount}")
        self.__update_minimum_balance()

    def withdraw(self, amount):
        if self.__is_frozen:
            print("Account is frozen.")
        elif amount > self.__balance + self.__overdraft_limit:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: {-amount}")
            self.__update_minimum_balance()

    def view_account_details(self):
        return f"Account Number: {self.number}\nOwner: {self.__owner}\nBalance: {self.__balance}"

    def change_owner(self, new_owner):
        self.__owner = new_owner

    def generate_statement(self):
        return "\n".join(self.__transaction_history)

    def set_overdraft_limit(self, limit):
        self.__overdraft_limit = limit

    def calculate_interest(self, rate):
        interest_amount = self.__balance * rate / 100
        self.deposit(interest_amount)
        self.__transaction_history.append(f"Interest: {interest_amount}")

    def freeze_account(self):
        self.__is_frozen = True

    def unfreeze_account(self):
        self.__is_frozen = False

    def get_transaction_history(self):
        return self.__transaction_history

    def set_minimum_balance(self, minimum):
        self.__minimum_balance = minimum

    def transfer_funds(self, target_account, amount):
        if self.__is_frozen:
            print("Account is frozen.")
        elif amount > self.__balance + self.__overdraft_limit:
            print("Insufficient funds.")
        else:
            target_account.deposit(amount)
            self.withdraw(amount)
            self.__transaction_history.append(f"Transfer: {amount} to {target_account.number}")

    def close_account(self):
        self.__balance = 0
        self.__transaction_history.clear()
        self.__is_frozen = True

    def __update_minimum_balance(self):
        if self.__balance < self.__minimum_balance:
            self.withdraw(self.__balance - self.__minimum_balance)

# creating an instance
account = Account(123456, "1234")

account.change_owner("John Doe")

account.deposit(500)

account.withdraw(200)

# Check balance
print(account.check_balance("1234"))

print(account.view_account_details())

# Generate statement
print(account.generate_statement())

# Set an overdraft limit
account.set_overdraft_limit(500)

# Calculate interest
account.calculate_interest(5)

# Freeze the account
account.freeze_account()
