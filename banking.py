
#Bank Account Simulation

accounts = {}

def create_account(account_number, name, **details):
    """Create an account with optional features like overdraft_limit."""
    accounts[account_number] = {"name":name, "details": details }
    print(accounts)

create_account((len(accounts) + 18273), "John", Balance = 43224, Branch = "Jos")
def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number in accounts:
        accounts[account_number]["details"]["Balance"] += amount
        print(f"The sum of {amount:,.2f} was deposited into account: {account_number} successfully!")
    else:
        return "Account not found!"
    print(accounts)
print(deposit(18273, 10))

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number in accounts:
        if amount <= accounts[account_number]["details"]["Balance"]:
            accounts[account_number]["details"]["Balance"] -= amount
        else:
            return "Insufficicient funds!"
    else:
        return "Account not found!"
    print(accounts)
print(withdraw(18274, 20400))

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    if from_acc in accounts:
        if amount <= accounts[from_acc]["details"]["Balance"]:
            accounts[from_acc]["details"]["Balance"] -= amount
            accounts[to_acc]["details"]["Balance"] += amount
            print(f"The sum of {amount:,.2f} was transfered into account: {to_acc} from account: {from_acc}")

        else:
            return "Insufficicient funds!"
    else:
        return "Account not found!"
    print(accounts)
transfer(18274, 18273, 10000)