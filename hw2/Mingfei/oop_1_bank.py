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


class Account:
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """


# Konstruktur
def _init_(self,idNumber,person,balance):
    self.balance = 0
    self.idNummer= idNumber
    self.holder = person
    self.balance = balance


# (a) Hooks
def _str_(self):

    res = "*** Account Information ***"
    res += "\n Account ID: " + str(self.idNummer)
    res += "\n Account Holder Name： " + str(self.holder)
    res += "\n Account Balance: " + str(self.balance)

    return res


# (b) Setter-Methode for holder
def set_holder(self,holder):
    if (not type(person) == str):
        raise TypeError
    if not re.match("\w + (\w+)*").person.strip():
        raise ValueError
    self.holder = person



#  (b)/ (c)  Methoden
def deposit(self, amount):

    self.balance += amount

def withdraw(self, amount):
    if self.balance > -1000:
        self.balance -= amount

def apply_interest(self):
    interst = 0.015 * self.balance
    self.balance += interst




# main Methode
if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    account1 = Account()
    account2 = Account()

    account1.__setattr__("A",3000)
    account2.__setattr__("B",5000)







    

