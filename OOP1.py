# Object Orientated Programming in Python Part 1
# Source: https://www.youtube.com/watch?v=JeznW_7DlB0

# self acts as a parameter that gets automatically referenced when we call
class Dog:

    def __init__(self, name, age):
        self.name = name  # self here refers to the particular instance of class dog thats being called upon
        self.age = age    # self.x = x here lets us reference d.name to the actual name that we inputted for the dog
        print(name)

    # talents

    def bark(self):
        print("bark")

    # attribute setters and getters

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Student added: " + student.get_name())
            return True
        print("Student not added: " + student.get_name())
        return False

    def get_average_grade(self):
        value = 0
        for x in self.students:
            value += x.get_grade()

        return value / len(self.students)

s1 = Student("Bob", 14, 55)
s2 = Student("Rob", 15, 93)
s3 = Student("Lob", 15, 76)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())