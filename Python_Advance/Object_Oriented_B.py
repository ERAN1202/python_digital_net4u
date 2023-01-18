class BankAccount():

    def __init__ (self,balance):
        self.balance = balance

def main():
    transferred_account = BankAccount(5000)

#בצורה הזו לעיל מעדכנית את מתודת האיתחול כך שתוכל לקבל כפרמטר "סכום כסף התחלתי"
# ונשנה את פעולת ההשמה של תכונת המופע כך שערכה יקבע עפ"י הפרמטר

class BankAccount_1():
    def __init__(self, balance=0):
        self.balance = balance

# לעלי ראינו יכולת בפייתון לקבוע ערכי ברירית מחדל לפרמטרים במתודות מחלקה
# בדוגמא לעיל זה במקרה לקוח שרוצה לפתוח חשבון בנק ואין לא כסף להעביר

class BankAccount_3():
    bank_name = "PayPy"

# בדודמא לעיל מדובר על תכונה של מחלקה שזו תכונה משותפת לכל חשבונות הבנק - שם הבנק למשל

def main():
    print(BankAccount_3.bank_name)

main()

class Sales:
    def __init__(self, money):
        self.money = money
        money = 100
val = Sales(123)
print(val.money)

class test:
    def __init__(self, a="hello world"):
        self._a = a
    def display(self):
        print(self._a)
obj = test()
obj.display()