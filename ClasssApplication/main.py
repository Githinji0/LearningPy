
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"HI, i am {self.name}")


mary = Person("Mary Johnson")
mary.talk()

john = Person("John Doe")
john.talk()