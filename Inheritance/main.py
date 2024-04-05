class Pets:
    def walk(self):
        print("Walking..")

    def eat(self):
        print("Eating..")


class Dog(Pets):
    def bark(self):
        print("The Dog is barking")


class Cat(Pets):
    def purr(self):
        print("The Cat is purring..")


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.eat()
cat.purr()
