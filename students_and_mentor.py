class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_h(self, lecturer, course, grade):
        """Выставления оценки лектору студентом, по курсу у этого студента
        Принимает на вход переменные rate_h(self, lecturer, course, grade)"""
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count

        res = f'Студент: \nИмя: {self.name}\nФамилия: {self.surname}\n' \
            f'Законченные курсы: {self.finished_courses}\n' \
            f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
            f'Средняя оценка за домашнее задание: {self.average_rating}'
        return res

    def __lt__(self, other):
        """Реализует сравнение через операторы '<, >' студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:  # преподаватели
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []  # курсы
        self.grades = {}
        self.average_rating = 0  # средняя оценка за лекции

    def __str__(self):
        """Возвращает характеристики экземпляра класса вида"""
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count

        res = f'Лектор: \nИмя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        """Реализует сравнение через операторы '<, >' лекторов между собой по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):  # эксперты, проверяющие домашние задания
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []  # курсы

    def __str__(self):
        res = f'Эксперт: \nИмя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        """Возможность выставления оценки студенту
        Принимает на вход переменные rate_hw(self, student, course, grade)"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# студенты
student1 = Student('Ruoy', 'Eman')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Иванов', 'Иван')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

# эксперты
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Петр', 'Петров')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

# оценки студентам
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Cit', 10)

reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Cit', 9)

# лекторы

lecturer1 = Lecturer('Яков', 'Яковлев')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Филип', 'Филипов')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

# оценки лекторам
student1.rate_h(lecturer1, 'Python', 10)
student1.rate_h(lecturer1, 'Git', 9)

student2.rate_h(lecturer2, 'Python', 10)
student2.rate_h(lecturer2, 'Git', 8)

print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)

print(reviewer2)

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 > student2}')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name}{lecturer2.surname} = {lecturer1 > lecturer2}')

student_list = [student1, student2]

lecturer_list = [lecturer1, lecturer2]


def verge_rating_students(student_list: [], course_name: ()):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if course_name in stud.courses_in_progress:
            sum_all += stud.average_rating
            count_all += 1
        if count_all == 0:
            return 0
        else:
            return sum_all / count_all


def verge_rating_lecturer(lecturer_list: [], course_name: ()):
    sum_all = 0
    count_all = 0
    for lec in lecturer_list:
        if course_name in lec.courses_attached:
            sum_all += lec.average_rating
            count_all += 1
        if count_all == 0:
            return 0
        else:
            return sum_all / count_all


print(
    f'Средняя оценка за домашнее задание у студентов по курсу Python: {verge_rating_students(student_list, "Python")}')


print(f"Средняя оценка за домашнее задание у студентов по курсу Git: {verge_rating_students(student_list, 'Git')}")


print(f"Средняя оценка за курсы у лекторов по курсу Git: {verge_rating_lecturer(lecturer_list, 'Git')}")


print(f"Средняя оценка за курсы у лекторов по курсу Python: {verge_rating_lecturer(lecturer_list, 'Python')}")
