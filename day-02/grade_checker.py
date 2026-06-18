# Video Link: https://youtu.be/lIId8IDP6TU?si=fSYHm6h4j-zIPIw9

a = int(input("Enter your marks: "))


if a>=0 and a<=100:
    if a >= 80:
        print("Grade: A+")
    elif a >= 70:
        print("Grade: A")
    elif a >= 60:
        print("Grade: A-")
    elif a >= 50:
        print("Grade: B")
    elif a > 40:
        print("Grade: C")
    elif a >= 0 and a <= 40:
        print("Grade: F")
else:
    print("Invalid marks. Please enter marks between 0 and 100.")

