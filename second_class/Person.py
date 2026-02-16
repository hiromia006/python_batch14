class Person:
    def __init__(self, age, height):   # fixed constructor
        self.age = age
        self.height = height

    def print_age(self):
        print(self.age)


p2 = Person(20, 30)
p2.print_age()   # no extra print()

