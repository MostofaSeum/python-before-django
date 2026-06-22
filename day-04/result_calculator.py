name = input("Enter students name: ")
mark1 = int(input("Enter students mark 1: "))
mark2 = int(input("Enter students mark 2: "))
mark3 = int(input("Enter students mark 3: "))


def calculate_total():
    total = mark1 + mark2 + mark3
    return total

def calculate_average():
    average = total / 3
    return average

def calculate_grade():
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    return grade

total = calculate_total()
average = calculate_average()
grade = calculate_grade()

def show_result():
    print("Name: ", name)
    print("Total: ", total)
    print("Average: ", average)
    print("Grade: ", grade)

show_result()