from typing import List


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):

    """Подават се различни стойности на __init__"""
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, 'test', 4.5, True)

    """Сравнява се дали стойностите които ще пази __init__ са правилните (в случая int)"""
    def test_initialization(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_data(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add_raises_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.add('test')

        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_add_successful(self):
        result = self.integer_list.add(10)
        self.assertEqual([1, 2, 3, 10], result)

    def test_remove_index_raises_index_error(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.remove_index(100)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_remove_index_successful(self):
        result = self.integer_list.remove_index(0)
        self.assertEqual(1, result)

    def test_get_raises_index_error(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.get(100)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_get_successful(self):
        result = self.integer_list.get(0)
        self.assertEqual(1, result)

    def test_insert_raises_index_error(self):
        with self.assertRaises(IndexError) as error:
            self. integer_list.insert(100, 3)

        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_raises_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.insert(0, 'test')

        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_insert_successful(self):
        self.integer_list.insert(0, 100)
        self.assertEqual([100, 1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_index(1), 0)



if __name__ == '__main__':
    unittest.main()
