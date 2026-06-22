
students = []

def add_student():
    print("\n--- Add New Student ---")
    try:
        student_id = int(input("Enter Student ID (Integer): "))
    except ValueError:
        print("Invalid ID. Please enter numbers only.")
        return

    # Check for duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists!")
            return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    department = input("Enter Department: ")
    
    try:
        cgpa = float(input("Enter CGPA: "))
    except ValueError:
        print("Invalid CGPA. Please enter a valid decimal number.")
        return

    # Create the student dictionary
    new_student = {
        "id": student_id,
        "name": name,
        "email": email,
        "department": department,
        "cgpa": cgpa
    }
    
    # Add to the list
    students.append(new_student)
    print(f" Student '{name}' added successfully!")


def view_students():
    print("\n--- All Registered Students ---")
    if not students:
        print("No students found in the database.")
        return
        
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Email: {student['email']} | Dept: {student['department']} | CGPA: {student['cgpa']}")


def search_student():
    print("\n--- Search Student by ID ---")
    try:
        search_id = int(input("Enter Student ID to search: "))
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    for student in students:
        if student["id"] == search_id:
            print("\n Student Found:")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Department: {student['department']}")
            print(f"CGPA: {student['cgpa']}")
            return
            
    print("Student not found.")


def update_email():
    print("\n--- Update Student Email ---")
    try:
        search_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Invalid input.")
        return

    for student in students:
        if student["id"] == search_id:
            new_email = input(f"Enter new email for {student['name']}: ")
            student["email"] = new_email
            print(" Email updated successfully!")
            return
            
    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    try:
        search_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    for student in students:
        if student["id"] == search_id:
            students.remove(student)
            print(f" Student {student['name']} has been removed.")
            return
            
    print("Student not found.")


def show_total_students():
    print("\n--- Total Students Counter ---")
    total = len(students)
    print(f"Total number of students: {total}")


# Main Interactive Menu Loop
def main():
    while True:
        print("\n=============================")
        print("  STUDENT MANAGEMENT SYSTEM  ")
        print("=============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Email")
        print("5. Delete Student")
        print("6. Show Total Number of Students")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_email()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_total_students()
        elif choice == "7":
            print("\nGoodbye! Exiting system.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()