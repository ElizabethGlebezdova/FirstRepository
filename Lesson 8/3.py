class human:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def say_name(self):
        print(f"My name is {self.name}")

    def say_age(self):
        print(f"I am {self.age} years old")

    def say_weight_and_height(self):
        print(f"My weight is {self.weight} and my height is {self.height}")

class Student(human):
    def __init__(self, name, age, weight, height, faculty, course, completed_homeworks):
        super().__init__(name, age, weight, height)
        self.faculty = faculty
        self.course = course
        self.completed_homeworks = completed_homeworks

    def say_about_studies(self):
        print(f"I am studying at the faculty of {self.faculty} in the {self.course} year")

    def say_about_grade(self):
        if (self.completed_homeworks == 7):
            print("I passed all my homework!!")
        elif (self.completed_homeworks == 0):
            print("I didn't pass any homework :c")
        else:
            print(f"I passed {self.completed_homeworks} homework assignments out of 7")

    def __cmp__ (self, other):
        if (self.completed_homeworks > other.completed_homeworks):
            return 1
        elif (self.completed_homeworks < other.completed_homeworks):
           return -1
        else:
            return 0


Mark = Student("Mark", 21, 60, 165, "IVT", 3, 4)
Sara = Student("Sara", 22, 56, 170, "Philology", 4, 7)
John = Student("John", 19, 64, 168, "Economics", 2, 0)
Anton = Student("Anton", 21, 70, 180, "IVT", 3, 4)
for student in (Mark, Sara, John):
    if (Anton.__cmp__(student) == 1):
        print(f"{Anton.name} has a larger number of completed homework assignments than {student.name}")
    elif (Anton.__cmp__(student) == -1):
        print(f"{student.name} has a larger number of completed homework assignments than {Anton.name}")
    else:
        print(f"{Anton.name} and {student.name} have the same number of completed homework assignments")