from src.domain import Student
from src.services import Services

class UiError(Exception):
    pass
class UI:
    def __init__(self):
        self._services=Services()

    def print_menu(self):
        while True:
            print("1. Add a new student.")
            print("2. Display students by grade.")
            print("3. Give bonuses.")
            print("4. Display students with a given string.")

            option=int(input("Please enter an option: "))
            try:
                if option==1:
                    student_id=input("Please enter the student ID: ")
                    name=input("Please enter the name: ")
                    attendance=input("Please enter the attendances: ")
                    grade=input("Please enter the grade: ")
                    student=Student(student_id, name, attendance, grade)
                    self._services.add_student(student)

                elif option==2:
                    students=self._services.decreasing_order()
                    for student in students:
                        print(student)

                elif option==3:
                    p=int(input("Enter the attendance: "))
                    b=int(input("Enter the bonus: "))

                elif option==4:
                    string=input("Please enter a string: ")
                    students=self._services.find_students(string)
                    for student in students:
                        print(student)
            except TypeError as ve:
                print(ve)




