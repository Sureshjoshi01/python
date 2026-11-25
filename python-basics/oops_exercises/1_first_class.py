# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

seltos = Vehicle(200,12)
print("Max Speed and Mileage for Seltos Car ")
print("Max Speed : ",seltos.max_speed," Mileage : ",seltos.mileage)

    