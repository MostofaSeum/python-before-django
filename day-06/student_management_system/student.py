class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major}"

    def to_csv(self):
        return f"{self.student_id},{self.name},{self.age},{self.major}\n"