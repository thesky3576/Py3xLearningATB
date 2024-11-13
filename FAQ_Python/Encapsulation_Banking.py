class bank :
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print("printing private variable: ",self.__private_var)

    def deposit_money(self,amount):
        self.balance += amount

    def __withdraw(self,amount):
            self.balance -= amount

    def __check_Balance(self):
        print("Your balance is : ",self.balance)

    def authenticate(self,flag):
        if flag :
            self.__check_Balance()
        else:
            print("not allowed")
    def authorise(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("not allowed")
fed = bank()
fed.deposit_money(1000)
fed.authenticate(True)
fed.authorise(True,100)
fed.authenticate(True)






