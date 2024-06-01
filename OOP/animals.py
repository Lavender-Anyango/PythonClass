# Polymorphism - the ability of objects of different classes to respond to the same method in different ways


class Animal:
    def move(self):
        pass

    def make_sound(self):
        pass


class Bird(Animal):
    def move(self):
        print("Flying")

    def make_sound(self):
        print("Chuck")


class Cat(Animal):
    def move(self):
        print("Walks")

    def make_sound(self):
        print("Meows")


class Fish(Animal):
    def move(self):
        print("swimming")

    def make_sound(self):
        print("Bop")