class Engine:
    def __init__(self, horse_power) -> None:
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size) -> None:
        self.size = size


class Car:
    def __init__(self, make, model, horse_power, wheel_size) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size)for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"


car = Car("Ford", "Mustang", 500, 18)
car2 = Car("Chevrolet", "Corvette", 670, 19)

print(car.display_car())
print(car2.display_car())
