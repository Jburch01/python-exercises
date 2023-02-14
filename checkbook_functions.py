import csv
import time
import os

def view():
    balance = get_balance()
    print(f"Your current balance is: {balance}")


def withdraw(num):
    balance = float(get_balance())
    if num > balance:
        print("Sorry you to broke for that!")
    else:
        balance -= num
        str(change_balance(balance))


def deposit(num):
    balance = float(get_balance())
    balance += num
    change_balance(balance)


def get_balance():
    if os.path.exists('checkbook.txt'):
        with open('checkbook.txt', 'r') as f:
            return f.read()
    else:
        with open('checkbook.txt', 'w') as f:
            f.write('0.00')
        with open('checkbook.txt', 'r') as f:
            return f.read()



def change_balance(amount):
    with open("checkbook.txt", 'w') as f:
        f.write(str(amount))


def check_input(a):
    return a.isdigit() or a.replace(".", "").isdigit()



