class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["age"], data["major"])

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major}"