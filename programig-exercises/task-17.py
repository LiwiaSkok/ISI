class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Carmen", 3, "Kremowy")
dog2 = Dog("Lexy", 5, "Brązowa")
dog3 = Dog("Franek", 2, "Biały")

dog1.sound()
dog2.sound()
dog3.sound()
