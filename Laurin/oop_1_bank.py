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
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        return amount
    def deposit(self, amount):
        self.balance += amount
    def __str__(self):
        res = "*** Account Info ***\n"
        res += "Account ID: " + str(self.number) + "\n"
        res += "Holder: " + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res
    def set_holder(self, person):
        if (not type(person) == str):
            raise TypeError
        if (not re.match("\W+( \W+)*", person.strip())):
            raise ValueError
        self.holder = person
    @staticmethod
    def accounts_info():
        print(Account.num_of_accounts, "accounts have been created")
    
    """ Konstruktor """
    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person
        Account.num_of_accounts += 1
    

if __name__ == "__main__":
    print("Welcome to the Python Bank!")


