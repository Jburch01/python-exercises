
def view():
    balance = get_balance()
    print(f"Your current balance is: {balance}")


def withdraw(num):
    balance = float(get_balance())
    if num > balance:
        print("sorry you to broke for that!")
    else:
        balance -= num
        str(change_balance(balance))


def deposit(num):
    balance = float(get_balance())
    balance += num
    change_balance(balance)


def get_balance():
    with open("checkbook.txt", 'r') as f:
        return f.read()


def change_balance(amount):
    with open("checkbook.txt", 'w') as f:
        f.write(str(amount))