"""
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 points)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 points)

e) Draw a UML diagram representing your Account class. (1 point)

"""

#! /usr/bin/python3

import re

class Account:
    """Klassenattribute"""
    num_of_accounts = 0

    """ Methoden der Klasse Account. """
    def withdraw(self, amount):
        '''withdraws an amount from an account - max negative is -3000'''
        if self.balance - amount < -3000:
            amount += -3000
            self.balance = -3000
        else:
            self.balance -= amount
        return amount

    def deposit(self, amount):
        '''to deposit a positive amount in the account'''
        if not amount < 1:
            self.balance += amount

    def __str__(self):
        '''string representation of the account object'''
        res = "*** Account Info ***\n"
        res += "Account ID: " + str(self.number) + "\n"
        res += "Holder: " + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        if self.formerholder != "":
            res += "Former Holder: " + self.formerholder + "\n"
        return res

    def set_holder(self, person):
        '''change account holder'''
        if (not type(person) == str):
            raise TypeError
        self.formerholder = self.holder
        self.holder = person

    def apply_interest(self):
        self.balance *= 1.015

    @staticmethod
    def accounts_info():
        '''prints the number of all created accounts at any moment'''
        print(str(Account.num_of_accounts) + " accounts have been created\n")
    
    """ Konstruktor """
    def __init__(self, num, person):
        '''initializes account with balance=0, number and holder variables'''
        self.balance = 0
        self.number = num
        self.holder = person
        self.formerholder = ""
        Account.num_of_accounts += 1
    

if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    nechniezesAcc = Account(1, "Nechniez")
    rellobeetsAcc = Account(2, "Rellobeet")
    ladislausesAcc = Account(3, "Ladislaus")
    fuerchtegottsAcc = Account(89, "Fuerchtegott")
    nechniezesAcc.deposit(3000)
    rellobeetsAcc.deposit(300)
    ladislausesAcc.deposit(8)
    rellobeetsAcc.withdraw(400)
    print(rellobeetsAcc)
    Account.accounts_info()
    nechniezesAcc.withdraw(1000)
    nechniezesAcc.apply_interest()
    print(nechniezesAcc)
    ladislausesAcc.deposit(-4000)
    print(ladislausesAcc)
    ladislausesAcc.withdraw(10)
    print(ladislausesAcc)
    fuerchtegottsAcc.set_holder(ladislausesAcc.holder)
    print(fuerchtegottsAcc)
    fuerchtegottsAcc.deposit(0)
    print(fuerchtegottsAcc)
    
    
    Account.accounts_info()

#   In Python Klassenvariablen (statische Variablen) und -methoden
#   auch in die "Klasse der Objekte" schreiben?
#   +-------------------------+
#   |         Account         |
#   |-------------------------|
#   |{static}num_of_accounts  |
#   |balance                  |
#   |holder                   |
#   |number                   |
#   |formerholder             |
#   |-------------------------|
#   |__init__(self,num,person)|
#   |__str__(self)            |
#   |apply_interest(self)     |
#   |set_holder(self,person)  |
#   |deposit(self,amount)     |
#   |withdraw(self,amount)    |
#   |{static}accounts_info()  |
#   +-------------------------+
