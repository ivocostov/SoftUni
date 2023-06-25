from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...

class Car(Vehicle):
    FUEL_INCREASE_WITH_AIR_CONDITIONER = 0.9

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Car.FUEL_INCREASE_WITH_AIR_CONDITIONER) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_INCREASE_WITH_AIR_CONDITIONER = 1.6

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.FUEL_INCREASE_WITH_AIR_CONDITIONER) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95
