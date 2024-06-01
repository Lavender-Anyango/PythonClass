class Vehicle:
    def __init__(self, make, color):
        self.make = make
        self.color = color





class Bus(Vehicle):
    def __init__(self, make, color, passengers):
        super().__init__(make, color)
        self.passengers= passengers

    def hoot(self):
        print("honk honk")

    def start_boarding(self):
        print("The bus is boarding")

    def accelerate(self):
        print("Accelerate start")
            

class Lorry(Vehicle):
    def __init__(self, make, color, max_load):
        super().__init__(make, color)
        self.max_load = max_load


    def unload(self):
        print("Unloading")



