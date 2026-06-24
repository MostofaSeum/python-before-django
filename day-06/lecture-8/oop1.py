#Video Link: https://youtu.be/HeW-D6KpDwY?si=_XfyE6rwN-QnpneR

# class Student:
#     def __init__(self):
#         print("This is constructor")
#     name = "Seum"
# s1 = Student()
# print(s1.name)

class Student:
    def __init__(self,fullname):
        print("This is constructor")
        self.name = fullname
s1 = Student("Seum")
print(s1.name)
