# from sololearn
# data hiding, class & static methods

# private method
# weakly private method _oneunderscore > marked as private
# strong private method __doubleunderscore > can't be accessed outside the class except with _Classname__privatemethod

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
         return "Account Balance: {}".format(self._balance)
    
    def deposit(self, amount):
        self.amount = amount
        self._balance += self.amount

acc = BankAccount(0)
acc.deposit(int(5))
print(acc)
