from MainProblem.project import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()


    def initialization(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[key])

        self.assertEqual(7, len(self.store.toy_shelf))


    def test_add_toy_if_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "Some toy")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")


    def test_add_toy_if_same_toy_already_on_shelf(self):
        self.store.add_toy("A", "Some toy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Some toy")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")


    def test_add_toy_if_shelf_already_taken(self):
        self.store.add_toy("A", "Some other toy")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Some toy")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")


    def test_add_toy_on_shelf_successful(self):
        self.store.add_toy("A", "Some toy")
        self.assertEqual("Some toy", self.store.toy_shelf["A"])


    def test_add_toy_returns_string(self):
        result = self.store.add_toy("A", "Some toy")
        self.assertEqual(result, "Toy:Some toy placed successfully!")


    def test_remove_toy_if_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Some toy")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")


    def test_remove_toy_if_no_toy_on_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Some toy")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")


    def test_remove_toy_successful(self):
        self.store.toy_shelf["A"] = "Some toy"
        self.store.remove_toy("A", "Some toy")
        self.assertEqual(None, self.store.toy_shelf["A"])


    def test_remove_toy_returns_string(self):
        self.store.toy_shelf["A"] = "Some toy"
        result = self.store.remove_toy("A", "Some toy")
        self.assertEqual(result, "Remove toy:Some toy successfully!")


if __name__ == '__main__':
    main()