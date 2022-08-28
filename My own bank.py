# Project 11 - Make your own bank, The Python Bible course, Ziyad Yehia
# Student Lukasz Swiatek Brzezinski

class Account: #creating parent classs called Account

    def __init__(self, name, balance, min_balance): #initiation and put the parameters

        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount): #function to add money to your account
        self.balance += amount

    def withdraw(self, amount): #function to withdraw your money, minimum balance has been maintain
        if  self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self): #to check how much money are on your account
        print("Account Balance: {}$".format(self.balance))

          

class Current(Account): #super class - creating your everyday account

    def __init__(self, name, balance): #this is the parameter you have to give to open account
        super().__init__(name, balance, min_balance = -1000) #this function pass the data to the main class upper


    def __str__(self):
        return "{}'s Current Account, balance: {}$, min_balance: {}$".format(self.name,self.balance,self.min_balance)
        #printing your accout you will get the form as upper (better readabillity)

class Save(Account): #super class creating account for savings

    def __init__(self,name,balance): #this is the parameter you have to give to open account
        super().__init__(name,balance,min_balance = 0) #this function pass the data to the main class upper

    def __str__(self):
        return "{}'s Save Account, Balance: {}$".format(self.name,self.balance)
        #printing your accout you will get the form as upper (better readabillity)

    
    def __del__(self):
        
        print("Account has been removed!")
