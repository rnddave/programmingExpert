## Student Class
"""
defined to keep track of students: 

- instance attribute called [name]

- property called [grade] that returns grade of that student
-- trying to set a grade should raise [VlaueErro] if the new grade is not between [0] and [100]

- a static method called [calculate_average_grade(students)]
-- accept list of [Student] objects
-- return the average grade for those students
-- if no student in list, then return [-1]

- class variable called [all_students]
-- stores student objects that have been created in the list 

- class method called [get_average_grade()]
-- return average grade for all created students

- class method called [get_best_student()]
-- return student object with the best grade out of all the currently created students
-- if no students created, the return [None]


"""

class Student:
    # - class variable called [all_students]
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.all_students.append(self)

    # - a static method called [calculate_average_grade(students)]
    @staticmethod
    def calculate_average_grade(students):
        # -- if no student in list, then return [-1]
        if len(students) == 0:
            return -1

        # -- return the average grade for those students
        total = 0
        for student in students:
            total += student.grade
        return total / len(students)


    # - class method called [get_average_grade()]
    @classmethod
    def get_average_grade(cls):
        # -- return average grade for all created students
        return cls.calculate_average_grade(cls.all_students)

    # - - class method called [get_best_student()]
    @classmethod
    def get_best_student(cls):
        best_student = None

        for student in cls.all_students:
            if best_student == None:
                best_student = student
        return best_student

