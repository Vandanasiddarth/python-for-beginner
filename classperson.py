class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")

person1 = Person(input(">"))
print(person1.name)
person1.talk()