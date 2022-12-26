class animals:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
    
    def say_name(self):
        print(f"I am {self.name} and I am a {self.__class__.__name__}")

    def type_of_animal(self):
        print(f"I am a {self.type}")
    def say_age(self):
        print(f"I am {self.age} years old")


class mammals(animals):
    def __init__(self, name, size, age, movement, habitation):
        super().__init__(name, size, age)
        self.movement = movement
        self.habitation = habitation
    
    def living (self):
        print(f"I live in {self.habitation}")

    def moving(self):
        print(f"I move with {self.movement}")


class human(mammals):
    def __init__(self, name, size, age, movement, habitation, hobby):
        super().__init__(name, size, age, movement, habitation)
        self.hobby = hobby

    def institution(self):
        if (self.age <= 0):
            print("I haven't been born yet")
        elif (self.age <= 7):
            print("I go to kindergarten")
        elif (self.age <= 18):
            print("I go to school")
        elif (self.age <= 25):
            print("I go to university")
        else:
            print("I go to work")
    
    def say_hobby(self):
        print(f"I am fond of {self.hobby}")


class cat(mammals):
    def __init__(self, name, size, age, movement, habitation, wool, eyes_color):
        super().__init__(name, size, age, movement, habitation)
        self.wool = wool
        self.eyes_color = eyes_color

    def type_of_wool(self):
        print(f"I have a {self.wool} wool")

    def say_about_eyes(self):
        print(f"My eyes are {self.eyes_color}")
    
    def say(self):
        print("Meow!")


class dog(mammals):
    def __init__(self, name, size, age, movement, habitation, ears):
        super().__init__(name, size, age, movement, habitation)
        self.ears = ears

    def type_of_ears(self):
        print(f"I have {self.ears} ears")

    def say(self):
        print("Bark!")

pupil = human("Jack", "big", 15, "2 legs", "Europe", "dance")
kitty = cat("Tom", "small", 1, "4 legs", "man's house", "short", "green")
puppy = dog("Sam", "small", 2, "4 legs", "man's house", "hanging")
for animals in (pupil, kitty, puppy):
    animals.say_name()
    animals.type_of_animal()
    animals.say_age()
    animals.living()
    animals.moving()
    if (animals.__class__.__name__ == "human"):
        animals.institution()
        animals.say_hobby()
    elif (animals.__class__.__name__ == "cat"):
        animals.type_of_wool()
        animals.say_about_eyes()
        animals.say()
    elif (animals.__class__.__name__ == "dog"):
        animals.type_of_ears()
        animals.say()
    print()