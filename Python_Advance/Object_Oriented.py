'''class  = הגדרת מחלקה בפייתון'''
'''נוסיף שם למחלקה ואז נקודותיים'''
'''
class BankAccount:

    def greet(self,name):
        print("Welcome", name)

def main():
    michals_account = BankAccount()
    michals_account.greet("Michal")
    amir_account = BankAccount()
    amir_account.greet("Amir")


main()

class BankAccount_2:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withrow (self, amount):
        self.balance -= amount
    def print_balance(self):
        print("Currnet balance is: ", self.balance)

def main():
    eyal_account = BankAccount()
    eyal_account.greet("Eyal")
    eyal = BankAccount_2()
    eyal.deposit(1200)
    eyal.withrow(200)
    eyal.print_balance()
'''
class Octopus:

    def __init__(self):
        self.age = 2
        self.name = "octavio"

    def birthday (self, new_age):
        self.age = new_age + 1
    def get_age(self):
        print("The octopus name is: ",self.name, "and is age is :", self.age)

    #def get_age (self, new_age):
    #    return self.age

def main():
    Octavio = Octopus()
    Octavio.birthday(4)
    Octavio.get_age()

main()
