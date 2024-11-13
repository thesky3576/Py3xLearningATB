class LoginPage :
    id = None
    password = None
    def __init__(self,id,password):
        self.id = id
        self.password = password

    def LogIn_Status(self):
        if self.password == "pass123":
            print("Login Successful for :",self.id)
        else:
            print("Login failed for :",self.id)

amitSharma = LoginPage("amitSharma@gmail.com","123")
amitSharma.LogIn_Status()

akashBhosale = LoginPage("akashbhosale@gmail.com","pass123")
akashBhosale.LogIn_Status()
