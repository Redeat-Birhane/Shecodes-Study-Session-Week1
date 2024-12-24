#Student managemnt system using classes
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        self.students.append(Student(name, age, grade))

    def view_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def delete_student(self, name):
        self.students = [student for student in self.students if student.name != name]

    def filter_students_by_grade(self, grade):
        filtered_students = [student for student in self.students if student.grade == grade]
        for student in filtered_students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

StudentSystesystem = StudentSystem()

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
            system.add_student(name, age, grade)
        case "2":
            system.view_students()
        case "3":
            name = input("Enter the name of the student to delete: ")
            system.delete_student(name)
        case "4":
            grade = input("Enter the grade to filter by: ")
            system.filter_students_by_grade(grade)
        case "5":
            break
        case _:
            print("Invalid choice. Please try again.")
