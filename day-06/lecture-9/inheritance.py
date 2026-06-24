class car:
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("Stop")

class ToyotaCar(car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

c1 = Fortuner("SUV")
c1.start()