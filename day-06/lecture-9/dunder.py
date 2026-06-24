#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show_complex(self):
        print(self.real, "i + ",self.img,"j")

    def __add__(self,other):
        return complex(self.real + other.real, self.img + other.img)

c1 = complex(1,2)
c2 = complex(3,4)
c1.show_complex()
c2.show_complex()
c3 = c1+c2
c3.show_complex()
    
