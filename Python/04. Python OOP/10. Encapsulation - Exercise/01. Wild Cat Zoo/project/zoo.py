from typing import List
from MainProblem.project import Animal
from MainProblem.project import Worker


class Zoo:
    def __init__(self, name: str, budget: float, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: float):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif price > self.__budget and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            #self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        # for fired_worker in self.workers:
        #     if worker_name == fired_worker:
        #         self.workers.remove(fired_worker)
        #         return f"{worker_name} fired successfully"
        # return f"There is no {worker_name} in the zoo"

        try:
            fired_worker = next(filter(lambda w: w.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(fired_worker)
        return f"{worker_name} fired successfully"

# обикаля заплатите на работниците и ги сумира

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

# пресмята колко ще струва да се грижим за животните

    def tend_animals(self):
        animals_tend_cost = sum(a.money_for_care for a in self.animals)
        if self.__budget < animals_tend_cost:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_tend_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: float):
        self.__budget += amount

# принтира животните по видове

    def animals_status(self):
        animals_info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [animals_info[a.__class__.__name__].append(str(a)) for a in self.animals]
        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(animals_info['Lion'])} Lions:",
            *animals_info['Lion'],

            f"----- {len(animals_info['Tiger'])} Tigers:",
            *animals_info['Tiger'],

            f"----- {len(animals_info['Cheetah'])} Cheetahs:",
            *animals_info['Cheetah'],
        ]

        return "\n".join(result)

# принтира работниците по позиции по друг начин различаващо се от това в горния method - animal_status

    def workers_status(self):
        workers_info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [workers_info[w.__class__.__name__].append(str(w)) for w in self.workers]  # w се прави на стринг за да може join в края на кода да си свърши работата
        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(workers_info['Keeper'])} Keepers:",
            *workers_info['Keeper'],                                 # ънпаква всички стойности на Keeper

            f"----- {len(workers_info['Caretaker'])} Caretakers:",
            *workers_info['Caretaker'],                              # ънпаква всички стойности на Caretaker

            f"----- {len(workers_info['Vet'])} Vets:",
            *workers_info['Vet'],                                    # ънпаква всички стойности на Vets
        ]

        return "\n".join(result)
