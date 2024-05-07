

class Dog:

    def __init__(self, name, age):
        self.name = name #attribute
        # whats the point of this attribute?
            # its stored permenatly for each specific object
            # self. can be referenced later on from methods in our class
        print(name)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
d.set_age(23)
print(d.get_age())

 



