#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY

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


#Multiple inheritence
class a:
    def printa(self):
        print("I am A")
class b:
    def printb(self):
        print("I am B")
class c(a,b):
    def printc(self):
        print("I am C")

obj = c()
obj.printa()
obj.printb()
obj.printc()



# class car:
#     @staticmethod
#     def start():
#         print("Start")
#     @staticmethod
#     def stop():
#         print("Stop")

# class ToyotaCar(car):
#     def __init__(self,brand):
#         self.brand = brand
#         print("The brand is ", brand)

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type
#         super().__init__("Valo")
#         print("The type is ", type)
        

# c1 = Fortuner("SUV")