import os
from student import Student


students_dict = {}


def load_data():
    if os.path.exists("data.txt"):
        with open("data.txt", "r") as f:
            for line in f:
                if line.strip():
                    data = line.strip().split(",")
                    student_id = int(data[0])
                    students_dict[student_id] = Student(student_id, data[1], int(data[2]), data[3])

def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id in students_dict:
            print("Student ID already exists!")
            return
        
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        major = input("Enter Major: ")
        
        new_student = Student(student_id, name, age, major)
        students_dict[student_id] = new_student
        print("Student " + name + " added successfully.")
    except ValueError:
        print("Invalid input. ID and Age must be integers.")

def view_all_students():
    if not students_dict:
        print("No students found.")
    else:

        for student in students_dict.values():
            print(student)

def search_student():
    try:
        search_id = int(input("Enter ID to search: "))
        if search_id in students_dict:
            print("Found:", students_dict[search_id])
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input.")

def delete_student():
    try:
        search_id = int(input("Enter ID to delete: "))
        if search_id in students_dict:
            del students_dict[search_id]
            print("Student deleted.")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input.")

def save_data():
    with open("data.txt", "w") as f:
        for student in students_dict.values():
            f.write(student.to_csv())
    print("Data saved successfully.")

def main():
    load_data()
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save and Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 5.")

if __name__ == "__main__":
    main()