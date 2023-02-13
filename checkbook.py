from checkbook_functions import *


def run_atm():
    inquiry = True
    while inquiry:
        question = input("What would you like to do? \n\n"
                         "1) View current balance\n"
                         "2) Record a debit (withdraw)\n"
                         "3) Record a credit (deposit)\n"
                         "4) exit\n")
        if question == '1':
            view()
        elif question == '2':
            amount = input("How much would you like to withdraw? ")
            withdraw(float(amount))
        elif question == '3':
            amount = input("How much would you like to deposit? ")
            deposit(float(amount))
        elif question == '4':
            balance = get_balance()
            print(f"Your ending balance is: {balance} \n Thanks have a good day! Goodbye")
            inquiry = False
        else:
            print("Not a valid option, please try again")
            pass


run_atm()
