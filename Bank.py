class Account(object):
    def __init__(self):
        self.value = 0

    def initialdeposite(self):
        initdepo = float(input("What is your initial deposit? "))
        self.value += initdepo

    def deposit(self):
        depovalue = float(input("how much would you like to deposite? "))
        self.value += depovalue
        
        
    def withdrawal(self):
        withdrawvalue = float(input("How much would you like to withdrawl? "))
        if withdrawvalue > self.value:
            print ("please stay within your balance")

        else:
            self.value -= withdrawvalue
        

    def balance(self):
        print ("your current Balance is :$%.2f" %float(self.value))

a=Account()
a.initialdeposite()
a.balance()

print(" would you like to make a deposit or witdrawal? \n Select 1 for deposit or 2 for withdraw.")

while True:
    x = int(input())
    if x == 1:
        
        a.deposit()
        a.balance()
        break

    elif x == 2:
        
        a.withdrawal()
        a.balance()
        break

    else:
        print(" please select 1 or 2")     




