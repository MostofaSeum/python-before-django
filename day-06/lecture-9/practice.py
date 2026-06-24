#Video Link: https://youtu.be/bAwmZVJeO5s?si=0I5ZWyJuqtAvqenY

#Question 1
# class Circle:
#     def __init__(self,r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r

#     def perimeter(self):
#         return 2 * 3.14 * self.r
    
# circle1 = Circle(5)
# print("Area of circle is: ",circle1.area())
# print("Perimeter of circle is: ",circle1.perimeter())


#Question 2
class Employee:
    def __init__(self,salary,role,department):
        self.salary = salary
        self.role = role
        self.department = department
    
    def show_details(self):
        print("Employee Salary: ",self.salary)
        print("Employee Role: ",self.role)
        print("Employee Department: ",self.department)
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)

    
class Engineer(Employee):
    def __init__(self,salary,role,department,name, age):
        self.name = name
        self.age = age
        super().__init__(salary,role,department)


    


eng1 = Engineer("5000","developer","IT","Seum",25)
eng1.show_details()

    
    
