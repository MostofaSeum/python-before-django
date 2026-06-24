#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY

class person:
    name = "Anonymus"

    @classmethod
    def change_name(cls, name):
        cls.name = name

person.change_name("Seum")
print(person.name)