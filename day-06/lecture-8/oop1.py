#Video Link: https://youtu.be/HeW-D6KpDwY?si=_XfyE6rwN-QnpneR

# class Student:
#     def __init__(self):
#         print("This is constructor")
#     name = "Seum"
# s1 = Student()
# print(s1.name)



# class Student:
#     college_name = "ABC College" #class attribute
#     def __init__(self,fullname):#instance attribute
#         print("This is constructor")
#         self.name = fullname
# s1 = Student("Seum")
# print(s1.college_name)
# print(s1.name)



class Student:
    college_name = "ABC College" #class attribute
    def __init__(self,fullname):#instance attribute
        print("This is constructor")
        self.name = fullname
    def hello(self):
        print("Hello", self.name)
s1 = Student("Seum")
print(s1.college_name)
print(s1.name)
s1.hello()