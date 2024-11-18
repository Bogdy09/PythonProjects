class Student:
    def __init__(self, student_id:str, name:str, attendance:str, grade):
        self._student_id=student_id
        self._name=name
        self._attendance=attendance
        self._grade=grade



    def get_student_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_attendance(self):
        return self._attendance

    def get_grade(self):
        return int(self._grade)

    def __str__(self):
        return "ID: "+self._student_id+" Name: "+self._name+" Attendances: "+self._attendance+" Grade: "+self._grade

