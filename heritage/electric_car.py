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

    def update_odometer(self, mileage):
        if mileage >= self.kilometrage:
            self.kilometrage = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.kilometrage += miles

new_car = Car('bmw', 'x6', 2020, '0')
print(new_car.get_des_name())
new_car.distance()

class ElectronicCars(Car):
    def __init__(self, make, model, year, kilometrage):
        super().__init__(make, model, year, kilometrage)
        
my_bmw = ElectronicCars('bmw', 'x7', 2022, '0')
print(my_bmw.get_des_name())