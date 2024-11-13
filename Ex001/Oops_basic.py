from queue import PriorityQueue
from xml.dom.minidom import ProcessingInstruction


class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        if self.b != 0 :
            return self.a / self.b
        else:
            print("Error! Cant divide by zero")
            return None
new_obj = calc(10,5)
print(f"Addition of given numbers is :", new_obj.sum())
print(f"subtraction of given numbers is : {new_obj.sub()}")
print(f"Multiplication of given numbers is : {new_obj.mult()}")
print(f"division of given numbers is : {new_obj.div()}")



