from exception import RichMaximumException

class Group:
    def __init__(self, number, limit = 10):
        self.number = number
        self.limit = limit
        self.group = set()

    def add_student(self, student):
        if len(self.group) == self.limit:
            raise RichMaximumException(self.number)

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group.copy():
            if last_name in str(student):
                return student

    def __str__(self):
        group = f'Number:{self.number}'

        for student in self.group:
            group += f'\n{student}'

        return group
