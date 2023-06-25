import unittest

from MainProblem.project import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Lucky', 'Dog', 'Woof')

    def test_initialization(self):
        self.assertEqual(self.mammal.name, 'Lucky')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'Woof')
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_sound(self):
        mammal_sound = self.mammal.make_sound()
        self.assertEqual(mammal_sound, f"{self.mammal.name} makes {self.mammal.sound}")

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        mammal_info = self.mammal.info()
        self.assertEqual(mammal_info, f"Lucky is of type Dog")


if __name__ == '__main__':
    unittest.main()

