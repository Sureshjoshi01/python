class Vehicle:
    color = 'white' 
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print("Color:", school_bus.color, "Vehicle name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)

audi_car = Car("Audi Q5", 240, 18)
print("Color:", audi_car.color, "Vehicle name:", audi_car.name, "Speed:", audi_car.max_speed, "Mileage:", audi_car.mileage)