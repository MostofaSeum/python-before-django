import json
import os
from student import Student

FILE_NAME = "data.txt"
students_list = []

def load_data():
    global students_list
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                students_list = [Student.from_dict(item) for item in data]
                print(f"Successfully loaded {len(students_list)} students.")
        else:
            print("No existing data file found. Starting fresh.")
    except Exception as e:
        print(f"Error loading data: {e}")

def save_data():
    try:
        with open(FILE_NAME, "w") as file:
            dict_list = [student.to_dict() for student in students_list]
            json.dump(dict_list, file, indent=4)
            print("Data successfully saved to file.")
    except Exception as e:
        print(f"Error saving data: {e}")

def add_student():
    student_id = input("Enter Student ID: ")
    
    if any(s.student_id == student_id for s in students_list):
        print("Error: A student with this ID already exists.")
        return

    name = input("Enter Name: ")
    
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
            
    major = input("Enter Major: ")

    new_student = Student(student_id, name, age, major)
    students_list.append(new_student)
    print(f"Student {name} added successfully!")

def view_all_students():
    if not students_list:
        print("No students in the system.")
        return
    
    print("\n--- Student List ---")
    for student in students_list:
        print(student)
    print("--------------------")

def search_student():
    search_id = input("Enter Student ID to search: ")
    for student in students_list:
        if student.student_id == search_id:
            print("\nStudent Found:")
            print(student)
            return
    print("Student not found.")

def update_student():
    search_id = input("Enter Student ID to update: ")
    for student in students_list:
        if student.student_id == search_id:
            print("Leave the field blank if you do not want to update it.")
            
            new_name = input(f"Enter new name (current: {student.name}): ")
            if new_name:
                student.name = new_name
                
            new_age = input(f"Enter new age (current: {student.age}): ")
            if new_age:
                try:
                    student.age = int(new_age)
                except ValueError:
                    print("Invalid age entered. Keeping old age.")
                    
            new_major = input(f"Enter new major (current: {student.major}): ")
            if new_major:
                student.major = new_major
                
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student():
    search_id = input("Enter Student ID to delete: ")
    for i, student in enumerate(students_list):
        if student.student_id == search_id:
            del students_list[i]
            print("Student deleted successfully!")
            return
    print("Student not found.")

def main():
    load_data()
    
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Save Data to File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            save_data()
        elif choice == '7':
            print("Saving data before exiting...")
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()