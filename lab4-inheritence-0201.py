class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    # inherits whats inside of Pet
    def speak(self):
        print("meow")

class Dog:

    def speak(self):
        print("bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.speak()