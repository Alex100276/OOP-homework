class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Студент: \nИмя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\nЗаконченные ' \
              f'курсы: {self.finished_courses}\nКурсы в процессе ' \
              f'изучения: {self.courses_in_progress}\nОценки: {self.grades}'
        return res

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

    def __str__(self):
        res = f'Лектор: \nИмя: {self.name}\nФамилия: {self.surname}\nПрикрепленные ' \
              f'курсы: {self.courses_attached}\nОценки: {self.grades}'
        return res


class Reviewer(Mentor):  # эксперты, проверяющие домашние задания
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []  # курсы

    def __str__(self):
        res = f'Эксперт: \nИмя: {self.name}\nФамилия: {self.surname}\nПрикрепленные ' \
              f'курсы: {self.courses_attached}'
        return res

    def rate_hw(self, student, course, grade):
        """Реализует возможность выставления оценки студенту,
        или возвращает ошибку.
        Принимает на вход переменные rate_hw(self, student, course, grade)"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# студенты
student1 = Student('Ruoy', 'Eman', 'man')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Иванов', 'Иван', 'man')
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

student1.rate_h(lecturer1, 'Python', 10)
student1.rate_h(lecturer1, 'Git', 10)

lecturer2 = Lecturer('Филип', 'Филипов')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

student1.rate_h(lecturer1, 'Python', 9)
student1.rate_h(lecturer1, 'Git', 10)

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
