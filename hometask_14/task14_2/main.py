from group import Group
from exception import RichMaximumException
from student import Student

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Female', 22, 'Maria', 'Lasso', 'AN147')
    st4 = Student('Male', 22, 'John', 'McLane', 'AN149')

    try:
        gr = Group('PD1')
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        print(gr)
        assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
        assert gr.find_student('Jobs2') is None

        gr.delete_student('Taylor')
        print(gr)


    except RichMaximumException as error:
        print(error)

if __name__ == '__main__':
    main()