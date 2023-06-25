import unittest
from car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Peugeot", "406", 6, 70)

    def test_initialization(self):
        self.assertEqual(self.car.make, "Peugeot")
        self.assertEqual(self.car.model, "406")
        self.assertEqual(self.car.fuel_consumption, 6)
        self.assertEqual(self.car.fuel_capacity, 70)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""

        self.assertEqual(str(error.exception), "Make cannot be null or empty!")

    def test_make_successful(self):
        self.car.make = "Citroen"
        self.assertEqual(self.car.make, 'Citroen')

    def test_model_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ''

        self.assertEqual(str(error.exception), "Model cannot be null or empty!")

    def test_model_successful(self):
        self.car.model = "Berlingo"
        self.assertEqual(self.car.model, 'Berlingo')

    def test_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0

        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_successful(self):
        self.car.fuel_consumption = 4
        self.assertEqual(self.car.fuel_consumption, 4)

    def test_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0

        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_successful(self):
        self.car.fuel_capacity = 50
        self.assertEqual(self.car.fuel_capacity, 50)

    def test_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1

        self.assertEqual(str(error.exception), "Fuel amount cannot be negative!")

    def test_fuel_amount_successful(self):
        self.car.fuel_amount = 30
        self.assertEqual(self.car.fuel_amount, 30)

    def test_refuel_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)

        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_over_capacity_successful(self):
        refuel_amount = 100
        self.assertTrue(refuel_amount > self.car.fuel_capacity)
        self.assertEqual(self.car.fuel_capacity, 70)

    def test_drive_raises_exception(self):
        driving_distance = 1000
        with self.assertRaises(Exception) as error:
            self.car.drive(driving_distance)

        self.assertTrue(driving_distance > self.car.fuel_amount)
        self.assertEqual(str(error.exception), "You don't have enough fuel to drive!")

    def test_drive_successful(self):
        self.car.fuel_amount = 70
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 64)



if __name__ == '__main__':
    unittest.main()
