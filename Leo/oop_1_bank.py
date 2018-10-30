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

    # Konstruktor
    def __init__(self, num, name):
        """Erzeugt ein Account-Objekt"""

        self.balance = 0
        self.number = num
        self.holder = name

    #Methoden
    def __str__(self):
        """Gibt die Daten eines Accounts als String zurück"""

        res = "*** Account Informationen ***\n"
        res += "Account-ID: " + str(self.number) + "\n"
        res += "Inhaber: " + self.holder + "\n"
        res += "Konstostand: " + str(self.balance) + "\n"
        return res

    def set_holder(self, name):
        """Ändert den Namen des Inhabers"""

        if name != self.holder:
            self.holder = name

    def withdraw(self, amount):
        """Reduziert den Kontostabd um den festgelegten Betrag bis maximal -1000"""

        if (self.balance - amount) < -1000:
            ramount = self.balance + 1000
            self.balance = -1000
            return ramount
        else:
            self.balance -= amount
            return amount

    def deposit(self, amount):
        """Erhöt den Kontostand um den festgelegten Betrag"""

        self.balance += amount
        return self.balance

    def apply_interest(self):
        """Erhöht den Kontostand um 1,5%, wenn dieser Positiv ist"""

        if self.balance >= 0:
            self.balance = round(self.balance *1.015)



if __name__ == "__main__":
    print("Welcome to the Python Bank!")

    leosAcc = Account(1, "Leo")
    laurinsAcc = Account(2, "Laurin")
    haotiensAcc = Account(3, "Haotien")

    leosAcc.deposit(4000)
    laurinsAcc.deposit(1000)
    haotiensAcc.deposit(3000)

    print(leosAcc, laurinsAcc, haotiensAcc)

    leosAcc.withdraw(6000)
    laurinsAcc.apply_interest()
    haotiensAcc.set_holder("Mingfei")
    haotiensAcc.withdraw(3500)

    print(leosAcc, laurinsAcc, haotiensAcc)


