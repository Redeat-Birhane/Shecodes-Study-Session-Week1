#Student list management systtem
students = []

def add_student(name, age, grade):
    students.append({"name": name, "age": age, "grade": grade})

def view_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def delete_student(name):
    for student in students:
      if student["name"]==name:
        del student

def filter_students_by_grade(grade):
    filtered_students = [student for student in students if student['grade'] == grade]
    for student in filtered_students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

while True:
    print("\nMenu:")
    print("1. Add a student")
    print("2. View all students")
    print("3. Delete a student")
    print("4. Filter students by grade")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    match choice:
      case "1":
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        grade = input("Enter student's grade: ")
        add_student(name, age, grade)
      case "2":
        view_students()
      case "3":
        name = input("Enter the name of the student to delete: ")
        delete_student(name)
      case "4":
        grade = input("Enter the grade to filter by: ")
        filter_students_by_grade(grade)
      case "5":
        break
      case _:
        print("Invalid choice. Please try again.")
