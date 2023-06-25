import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    """ Test if the worker is initialized with the correct name, salary, and energy """
    def test_worker_initialization(self):
        worker = Worker('Ivo Kostov', 1000, 10)
        self.assertEqual(worker.name, 'Ivo Kostov')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)


    """ Test if the worker's energy is incremented after the rest method is called """
    def test_worker_energy_increment(self):
        worker = Worker('Ivo Kostov', 1000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    """ Test if an error is raised if the worker tries to work with negative energy or equal to 0 """
    def test_worker_works_with_invalid_values(self):
        worker = Worker('Ivo Kostov', 1000, -1)  # подава се с невалидна стойност -1 за да работи
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    """ Test if the worker's money is increased by his salary correctly after the work method is called """
    def test_worker_salary(self):
        worker = Worker('Ivo Kostov', 1000, 10)
        worker.work()
        self.assertEqual(worker.money, 1000)

    """ Test if the worker's energy is decreased after the work method is called """
    def test_worker_energy_decrease(self):
        worker = Worker('Ivo Kostov', 1000, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    """ Test if the get_info method returns the proper string with correct values """
    def test_worker_get_info(self):
        worker = Worker('Ivo Kostov', 1000, 10)
        self.assertEqual(worker.get_info(), f'Ivo Kostov has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
