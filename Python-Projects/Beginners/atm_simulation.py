# The ATM Simulation project is a practical and engaging exercise where you create
# a simple ATM system. The system allows users to check their balance, deposit
# money, and withdraw funds. This project introduces basic Object-Oriented
# Programming (OOP) concepts by encapsulating the ATM's logic within a class and
# handling user interactions through a controller class.
# Optional
# Optional Enhancements
# • Implement a PIN system where users must enter their PIN before accessing
# the ATM functions.
# • Add a feature to keep track of all transactions (deposits and withdrawals) and
# allow users to view their transaction history.
# • Allow the system to handle multiple user accounts, enabling users to log in
# and manage their individual balances.


import csv
class Atm:
    

    def check_pin(self):
        print("Enter your Account number : ")
        account = input()
        if len(account) < 4 or not account.isdigit():
            print("Invalid Account")
            return False,None,None
        print("Enter your 4 digit pin : ")
        pin = input()
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN")
            return False,None,None
        with open("atm_records.csv","r",newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == account and row[1] == pin:
                    print("Welcome ",row[2])
                    return True,row[3],account
        return False,None,None

                    
    def check_balance(self):
        is_valid,balance,account = self.check_pin()
        if is_valid == False:
            print("Invalid Account Number or PIN")
        else:
            print("Your current balance : ",balance)

    def deposit(self):
        rows = []
        is_valid,balance,account = self.check_pin()
        if is_valid == False:
            print("Invalid Account Number or PIN")
        else:
            print("Your current balance : ",balance)
            print("Enter the amount to be deposited : ")
            try:
                amount = int(input())
            except ValueError:
                print("Please enter a valid number")
                return
            if amount <= 0:
                print("Amount must be greater than zero")
                return
            with open("atm_records.csv","r",newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if  row[0] == account:
                        row[3] = str(int((row[3]))+ amount)
                        print("Amount deposited successfully. Current Balance : ",row[3])
                    rows.append(row)
            with open("atm_records.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                return
    
   
    def withdraw(self):
        rows = []
        is_valid,balance,account = self.check_pin()
        if is_valid == False:
            print("Invalid Account Number or Pin")
        else:
            print("Enter amount to be withdraw : ")
            try:
                amount = int(input())
            except ValueError:
                print("Please enter a valid number")
                return
            if int(amount) > int(balance):
                print("Insufficient Balance")
            elif amount <= 0:
                print("Amount must be greater than zero")
                return
            else:
                balance = int(balance)
                amount  = int(amount)
                print(balance)
                balance = balance - amount
                with open("atm_records.csv","r",newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if  row[0] == account:
                            row[3] = str(balance)
                            print("Amount Withdrawn successfully. Current Balance : ",row[3])
                        rows.append(row)
                with open("atm_records.csv","w",newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

    def main(self):
        print("###############################################")
        print("#             ATM MACHINE                     #")
        print("###############################################")
        
        while True:
            print("Choose from Below options : ")
            print("1. Check Balance")
            print("2. Deposit Amount")
            print("3. Withdraw Amount")
            try:
                choice = int(input())
            except ValueError:
                print("Invalid Choice")
                continue
            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            else:
                print("Invalid Choice")
            exit_choice = input("Continue? Y/N")
            if exit_choice.upper() == "N":
                return
            
atm = Atm()
atm.main()
