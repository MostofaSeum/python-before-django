#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY

class studnet:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3

student1 = studnet(90,80,70)
print(student1.percentage)
