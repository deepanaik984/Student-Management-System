import csv
students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    save_students()
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n----- Student Records -----")
        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("--------------------------")

def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False

    for student in students:
        if student["ID"] == search_id:
            print("\nStudent Found")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            found = True
            break

    if not found:
        print("Student not found.")

def update_student():
    update_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == update_id:
            print("Student Found!")

            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            print("Student details updated successfully!")
            return

    print("Student not found.")
    save_students()

def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")
    save_students()
def save_students():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Age", "Course"])

        for student in students:
            writer.writerow([
                student["ID"],
                student["Name"],
                student["Age"],
                student["Course"]
            ])

def load_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        pass
load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")