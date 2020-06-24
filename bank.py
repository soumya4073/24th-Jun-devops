class Customer:
  
    ''' This program devloped by soumya mohanty'''
    bankname = "SOUMYA BANK"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance


    def deposite(self,amount):
        self.balance = self.balance+amount
        print("After deposite the amount is:",self.balance)


    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds")

        else:
            self.balance = self.balance-amount
            print("After withdraw balance is:",self.balance)

print("Welcome to",Customer.bankname)

name = input("Enter your name:")
print("Thank you Mr.",name)

c = Customer(name)
while True:
    print("d-deposite\nw-withdrawl\ne-Exit")
    option = input("Chose your option from above:")

    if option.lower()=="d":
        amount = float(input("Enter amount to deposite:"))
        c.deposite(amount)
    elif option.lower()=="w":
        amount = float(input("Enter amount to withdrawl:"))
        c.withdraw(amount)
    elif option.lower()=="e"
        print("Thanks for Banking with us")

    else:
        print("You have chosen Invalid option...Plz chose valid option
