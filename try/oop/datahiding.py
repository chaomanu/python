# data hiding challenge from sololearn
# private methods & attributes
# weakly private _oneunderscore > marked as private
# strongly private __doubleunderscore > can't be accessed outside the class except with _Classname__privatemethod

# weakly private
class BankAccount:
    def __init__(self, balance):
        self._balance = balance # balance marked as private

    def __repr__(self):
         return "Account Balance: {}".format(self._balance)
    
    def deposit(self, amount):
        self.amount = amount
        self._balance += self.amount

acc = BankAccount(0)
acc.deposit(int(5))
print(acc)
print(acc._balance)


#strongly private
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # balance marked as strongly private

    def __repr__(self):
         return "Account Balance: {}".format(self.__balance)
    
    def deposit(self, amount):
        self.amount = amount
        self.__balance += self.amount

acc = BankAccount(0)
acc.deposit(int(10))
print(acc)
print(acc._BankAccount__balance)
try:
    print(acc.__balance)
except(AttributeError):
    print("can't print private method attribute like that")