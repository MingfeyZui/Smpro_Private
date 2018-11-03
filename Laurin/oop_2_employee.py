"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
"""
class Person:
    '''Eine Klasse aller Personen'''
    #=Konstruktor================================================
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.verstorben = False
    
    def happy_birthday(self):
        self.alter += 1

    def stirbt(self):
        self.versorbern = True

class Employee(Person):
    '''Eine Klasse, die alle Angestellten beschreibt'''
    #=Konstruktor================================================
    def __init__(self,name, alter, unternehmen, gehalt, stelle):
        Person.__init__(self, name, alter)
        self.unternehmen = unternehmen
        self.gehalt = gehalt
        self.stelle = stelle
        
    def __str__(self):
        res  = "*** Employee Info ***"
        res += "\nName: " + self.name
        res += "\nAlter: " + str(self.alter)
        res += "\nAngestellt bei: " + self.unternehmen
        res += "\nGehalt: " + str(self.gehalt) +"\n"
        return res
    
    def feuern(self):
        self.unternehmen = "N/A"

    def gehalt_erhoehen(self, amount):
        self.gehalt += amount

    def stelle_wechseln(self, neue_stelle):
        self.stelle = neue_stelle
    
    def isAngestellt(self):
        if self.versorbern or (self.unternehmen == "N/A"):
            return False
        return True

    def isAngestellt_bei(self, unternehmensname):
        if self.isAngestellt and (self.unternehmen == unternehmensname):
            return True
        return False

if __name__ == "__main__":
    print("Employee application")
    berta = Employee("Berta", 56, "IBM", 4200, "Executive Product Manager")
    berta.happy_birthday()
    print(berta)
    berta.gehalt_erhoehen(50)
    if berta.isAngestellt_bei("Google"):
        print(berta.name + " ist angestellt bei Google")
    else:
        print(berta.name + " ist nicht angestellt bei Google")
