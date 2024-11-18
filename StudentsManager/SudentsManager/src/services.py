from src.repository import Repository


class Services():
    def __init__(self):
        self._repo=Repository()

    def get_all(self):
        return self._repo.get_all_repo()

    def add_student(self, student):
        """
        It calls the function in the repository that adds a new student to the dictioanry
        :param student:
        :return: nothing
        """
        self._repo.add_student_repo(student)

    def decreasing_order(self):
        return self._repo.decreasing_order_repo()

    def find_students(self, string):
        return self._repo.find_students_repo(string)