#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY


# class student:
#     def __init__(self, name):
#         self.name = name
#         print("Hello", name)

# s1 = student("Seum")
# print(s1.name)
# del s1
# print(s1)


class bank:
    # def password_calling(self):
    #     password = 12345
    #     print(password)

    # def get_password(self):
    #     self.password_calling()
    def __hello(self):
        print("Hello")

    def get_hello(self):
        self.__hello()


a = bank()
a.get_hello()
