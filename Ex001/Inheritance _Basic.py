class grandma:
    def __init__(self, grandname):
        self.grandname = grandname
class mother(grandma):
    def __init__(self, mothername, grandname):
        self.mothername = mothername
        grandma.__init__(mothername, grandname)
class son(mother):
    def __init__(self,sonname, mothername, grandname):
        self.sonname = son
        mother.__init__(sonname,mothername,grandname)
    def printname(self):
        print('Grandma name :', self.grandname)
        print("Mother name :", self.mothername)
        print("Son name :", self.sonname)


