class car :
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def start_Engine(self):
        print("engine started")

    def drive(self):
        print(f"driving {self.brand} car having {self.color} color")
my_car = car("ferrari","red")
my_car.start_Engine()
my_car.drive()