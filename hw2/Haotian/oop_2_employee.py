"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
"""


class Employee:
    def __init__(self, n, a, s):
        """
        constructor, set name, age and salary
        """
        self.name = n
        self.age = a
        self.salary = s

    def set_age(self, new_a):
        """
        change employee age
        """
        self.age = new_a

    def set_salary(self, new_s):
        """
        change employee salary
        """
        self.salary = new_s

    def __str__(self):
        """
        returns a string when printing an object
        """
        res = "EMPLOYEE INFORMATION:"
        res += "\nName: "
        res += self.name
        res += "\nAge: "
        res += str(self.age)
        res += "\nSalary: $"
        res += str(self.salary)
        res += "\n"
        return res

if __name__ == "__main__":
    print("Stirnlappenbasilisk AG Employee application")
    tom = Employee("Tom Saywer", 9, 100)
    print("Tom Sawyer now works for Stirnlappenbasilisk AG")
    print("Information for Tom Sawyer as follows")
    print(tom)

    tom.set_age(10)
    print("Tom Sawyer is now " + str(tom.age) + ".")

    tom.set_salary(200)
    print("Promotion for Tom Sawyer, the salary is now $" + str(tom.salary) + ".")
