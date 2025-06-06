class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        return "Some generic animal sound."


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Meow!"


class Fox(Animal):
    def sound(self):
        return "Roar!"


def main():
    dog = Dog("Carmen", 5, "male", "Border collie")
    cat = Cat("Mila", 3, "female", "Persian")
    fox = Fox("Foxy", 2, "female")

    print(f"{dog.name} ({dog.breed}) says: {dog.sound()}")
    print(f"{cat.name} ({cat.breed}) says: {cat.sound()}")
    print(f"{fox.name} says: {fox.sound()}")

if __name__ == '__main__':
    main()
