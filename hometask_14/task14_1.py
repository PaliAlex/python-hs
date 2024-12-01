class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def show_info(self):
        self.__str__()

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Age: {self.age}, {self.gender}.'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self):
        return f"{super().__str__()} Record book - {self.record_book}"

class Group:
    def __init__(self, number, limit = 2):
        self.number = number
        self.limit = limit
        self.group = set()

    def add_student(self, student):
        if len(self.group) > self.limit:
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

class RichMaximumException(Exception):
    def __init__(self, group_number):
        self.group_number = group_number

    def __str__(self):
       return f"The maximum amount for group {self.group_number} students is reached."


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 22, 'Maria', 'Lasso', 'AN147')
st4 = Student('Male', 22, 'John', 'McLane', 'AN149')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
print(gr)

