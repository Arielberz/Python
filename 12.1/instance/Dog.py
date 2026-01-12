from Animal import Animal
class Dog(Animal):
    def bark(self):
        print("Woof Woof")
d = Dog("Buddy")
d.bark()
d.make_sound()