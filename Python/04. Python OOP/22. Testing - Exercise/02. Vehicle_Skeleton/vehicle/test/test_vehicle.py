import unittest
from MainProblem.project import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.0, 100.0)

    def test_fuel_consumption_const(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_initialization(self):
        self.assertEqual(self.vehicle.fuel, 10.0)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 100.0)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise_exception(self):
        self.vehicle.fuel = 0  # за да сме сигурни че няма достатъчно гориво
        kilometers = 100

        with self.assertRaises(Exception) as error:
            self.vehicle.drive(kilometers)

        self.assertEqual(str(error.exception), "Not enough fuel")

    def test_drive_successful(self):
        self.vehicle.drive(4)
        self.assertEqual(self.vehicle.fuel, 5)

    def test_refuel_raise_exception(self):
        refuel_amount = 1
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(refuel_amount)

        self.assertEqual(str(error.exception), "Too much fuel")

    def test_refuel_successful(self):
        self.vehicle.fuel = 0
        refuel_amount = 5
        self.vehicle.refuel(refuel_amount)
        self.assertEqual(self.vehicle.fuel, 5)

    def test_string_method(self):
        self.vehicle.horse_power = 100
        self.vehicle.fuel = 50
        self.vehicle.fuel_consumption = 10
        self.assertEqual(self.vehicle.__str__(),
                         f"The vehicle has 100 " +
                         f"horse power with 50 fuel left and 10 fuel consumption"
                         )


if __name__ == '__main__':
    unittest.main()
