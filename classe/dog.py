class Dog:
    """Une simple tentative de modéliser un chien."""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age 
    def sit(self):
        """assis a l'ordre"""
        print(f"{self.name} is sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
my_dog = Dog('Max', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")