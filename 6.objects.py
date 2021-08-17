
# Object Oriented Programming

class Dog:
    
    # Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    
    # Method
    def say_name(self):
        print(f"My name is {self.name}")


spot = Dog("Spot", 11, "Poodle") 

print(spot.age)

spot.say_name()


print('\n')


# Inheritance
class Pug(Dog):
    def __init__(self, name, age, breed, face):
        super().__init__(name, age, breed)
        self.face = face


    # Method
    def is_it_ugly(self):
        print(f"{self.name} has a {self.face} face")


pudge = Pug("Pudge", 12, "Pug", "cute") 

print(pudge.name)

pudge.is_it_ugly()