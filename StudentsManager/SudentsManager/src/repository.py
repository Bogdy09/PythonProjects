from src.domain import Student


class Repository:
    def __init__(self):
        self._data = {}
        self.load()

    def load(self):
        with open("students.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                (
                    student_id,
                    name,
                    attendance,
                    grade
                ) = line.split(",")

                student = Student(student_id, name, attendance, grade)
                self._data[student_id] = student

    def save(self):
        with open("students.txt", "w") as f:
            for student in self._data.values():
                f.write(
                f"{student.get_student_id()}, {student.get_name()}, {student.get_attendance()}, {student.get_grade()} {"\n"}"
                )

                def __init__(self, width: int = 6, height: int = 6):
                    self._width = width
                    self._height = height
                    self._board = [[' ' for _ in range(width)] for _ in range(height)]

                def __str__(self):
                    t = Texttable()

                    hrow = [' '] + [str(i + 1) for i in range(self._width)]
                    t.add_row(hrow)

                    for i in range(self._height):
                        t.add_row([chr(ord('A') + i)] + self._board[i])

                    return t.draw()

                def load(self):
                    with open("students.txt", "r") as f:
                        for line in f.readlines():
                            line = line.strip()
                            if line == "":
                                continue
                            (
                                student_id,
                                name,
                                attendance,
                                grade
                            ) = line.split(",")

                            student = Student(student_id, name, attendance, grade)
                            self._data[student_id] = student

                def save(self):
                    with open("students.txt", "w") as f:
                        for student in self._data.values():
                            f.write(
                                f"{student.get_student_id()}, {student.get_name()}, {student.get_attendance()}, {student.get_grade()} {"\n"}"
                            )

    def __init__(self, width: int = 6, height: int = 6):
        self._width = width
        self._height = height
        self._board = [[' ' for _ in range(width)] for _ in range(height)]

    def __str__(self):
        t = Texttable()

        hrow = [' '] + [str(i + 1) for i in range(self._width)]
        t.add_row(hrow)

        for i in range(self._height):
            t.add_row([chr(ord('A') + i)] + self._board[i])

        return t.draw()

    def load(self):
        with open("students.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                (
                    student_id,
                    name,
                    attendance,
                    grade
                ) = line.split(",")

                student = Student(student_id, name, attendance, grade)
                self._data[student_id] = student

    def save(self):
        with open("students.txt", "w") as f:
            for student in self._data.values():
                f.write(
                    f"{student.get_student_id()}, {student.get_name()}, {student.get_attendance()}, {student.get_grade()} {"\n"}"
                )

    def __init__(self, width: int = 6, height: int = 6):
        self._width = width
        self._height = height
        self._board = [[' ' for _ in range(width)] for _ in range(height)]

    def __str__(self):
        t = Texttable()

        hrow = [' '] + [str(i + 1) for i in range(self._width)]
        t.add_row(hrow)

        for i in range(self._height):
            t.add_row([chr(ord('A') + i)] + self._board[i])

        return t.draw()

    def load(self):
        with open("students.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                (
                    student_id,
                    name,
                    attendance,
                    grade
                ) = line.split(",")

                student = Student(student_id, name, attendance, grade)
                self._data[student_id] = student

    def save(self):
        with open("students.txt", "w") as f:
            for student in self._data.values():
                f.write(
                    f"{student.get_student_id()}, {student.get_name()}, {student.get_attendance()}, {student.get_grade()} {"\n"}"
                )
    def load_patterns(self):
        with open('patterns.txt','r') as f:
            lines=f.readlines()
        for line in lines:
            line=line.strip()
            if line=="":
                continue
            if ':' in line:
                pattern=line[:-1]
                self.__patterns[pattern]=[]
                column=0
            else:
                for i,cell in enumerate(line):
                    if cell=='X':
                        self.__patterns[pattern].append((column,i))
                column+=1

    def save_to_file1(self,board,file_name='save1.txt'):
        with open(file_name,'w') as f:
            for i,row in enumerate(board.board):
                string=''
                for j,val in enumerate(row):
                    string+=str(val)
                string+='\n'
                f.write(string)

                def __init__(self, width: int = 6, height: int = 6):
                    self._width = width
                    self._height = height
                    self._board = [[' ' for _ in range(width)] for _ in range(height)]

                def __str__(self):
                    t = Texttable()

                    hrow = [' '] + [str(i + 1) for i in range(self._width)]
                    t.add_row(hrow)

                    for i in range(self._height):
                        t.add_row([chr(ord('A') + i)] + self._board[i])

                    return t.draw()

                def load(self):
                    with open("students.txt", "r") as f:
                        for line in f.readlines():
                            line = line.strip()
                            if line == "":
                                continue
                            (
                                student_id,
                                name,
                                attendance,
                                grade
                            ) = line.split(",")

                            student = Student(student_id, name, attendance, grade)
                            self._data[student_id] = student

                def save(self):
                    with open("students.txt", "w") as f:
                        for student in self._data.values():
                            f.write(
                                f"{student.get_student_id()}, {student.get_name()}, {student.get_attendance()}, {student.get_grade()} {"\n"}"
                            )

                def load_patterns(self):
                    with open('patterns.txt', 'r') as f:
                        lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == "":
                            continue
                        if ':' in line:
                            pattern = line[:-1]
                            self.__patterns[pattern] = []
                            column = 0
                        else:
                            for i, cell in enumerate(line):
                                if cell == 'X':
                                    self.__patterns[pattern].append((column, i))
                            column += 1

                def save_to_file1(self, board, file_name='save1.txt'):
                    with open(file_name, 'w') as f:
                        for i, row in enumerate(board.board):
                            string = ''
                            for j, val in enumerate(row):
                                string += str(val)
                            string += '\n'
                            f.write(string)
    def get_all_repo(self):
        return list(self._data.values())

    def add_student_repo(self, student):
        """
        The function adds a student in the dictionary if there are no errors raised
        :param student:
        :return: nothing
        """
        if not student.get_student_id().isdigit():
            raise TypeError("Invalid ID!")
        name1 = student.get_name().split(" ")
        if len(name1) < 2:
            raise TypeError("Invalid name!")
        a=name1[0]
        b=name1[1]
        if len(a)<3 or len(b)<3:
            raise TypeError("Invalid name!")
        if not student.get_attendance().isdigit() or not int(student.get_attendance())>0:
            raise TypeError("Invalid attendance!")
        if not 0<=int(student.get_grade())<=10:
            raise TypeError("Invalid grade!")
        self._data[student.get_student_id()] = student
        self.save()


    def decreasing_order_repo(self):
        students=self.get_all_repo()
        sorted_students=sorted(students, key=lambda x: x.get_grade(), reverse=True)
        return sorted_students

    def find_students_repo(self, string):
        student=[]
        for i in self._data.values():
            if string in i.get_name():
                student.append(i)

        return student
