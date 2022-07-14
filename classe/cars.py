class Car:
    def __init__(self, make, model, year, kilometrage):
        self.make = make
        self.model = model
        self.year = year
        self.kilometrage = kilometrage
    
    def get_des_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def distance(self):
        print(f"{self.kilometrage}km au compteur")

new_car = Car('bmw', 'x6', 2022, '0')
print(new_car.get_des_name())
new_car.distance()