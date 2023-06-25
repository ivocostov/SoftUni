# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return 'Woof'
#
#
# class Cat(Animal):
#     def speak(self):
#         return 'Meow'
#
#
# class AnimalFactory:
#     def get_animal(self, animal_type):
#         if animal_type == 'dog':
#             return Dog()
#         elif animal_type == 'cat':
#             return Cat()
#         else:
#             return None
#
#
# factory = AnimalFactory()
# animal = factory.get_animal('dog')
# print(animal.speak())
#
# animal = factory.get_animal('cat')
# print(animal.speak())

########################################################################################################################

# """ SINGLETON IMPLEMENTATION """"
#
# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def some_business_logic(self):
#         pass
#
#
# singleton_1 = Singleton()
# singleton_2 = Singleton()
#
# print(singleton_1 is singleton_2)

########################################################################################################################

# """ ABSTRACT IMPLEMENTATION """"
#
#
# from abc import ABC, abstractmethod
#
#
# class Pizza(ABC):
#
#     @abstractmethod
#     def prepare(self):
#         ...
#
#
#     def bake(self):
#         print('baking pizza...')
#
#
#     def cut(self):
#         print('cutting pizza...')
#
#
#     def box(self):
#         print('boxing pizza...')
#
#
# class CheesePizza(Pizza):
#     def prepare(self):
#         print('Preparing Cheese Pizza...')
#
#
# class PepperonePizza(Pizza):
#     def prepare(self):
#         print('Preparing Pepperone Pizza...')
#
#
# class PizzaFactory(ABC):
#     @abstractmethod
#     def create_pizza(self):
#         ...
#
#
# class CheesePizzaFactory(PizzaFactory):
#     def create_pizza(self):
#         return CheesePizza()
#
#
# class PepperonePizzaFactory(PizzaFactory):
#     def create_pizza(self):
#         return PepperonePizza()
#
#
# factory = PepperonePizzaFactory()
# pizza = factory.create_pizza()
# pizza.prepare()
# pizza.bake()
# pizza.cut()
# pizza.box()


########################################################################################################################

# """ STRUCTURAL DESIGN - FACADE IMPLEMENTATION """
#
# class CPU:
#     def freeze(self):
#         print('Freezing CPU...')
#
#
#     def jump(self, position):
#         print(f'Jumping to position {position}...')
#
#
#     def execute(self):
#         print('Executing CPU commands...')
#
#
# class Memory:
#     def load(self, position, data):
#         print(f'Loading data {data} into memory position {position}...')
#
#
# class HardDrive:
#     def read(self, position, size):
#         print(f'Reading {size} bytes from hard drive position {position}...')
#
#
# class Computer:                    # FACADE започва от тук като прикрива по сложния код отгоре ( действа като фасада )
#     def __init__(self):
#         self.cpu = CPU()
#         self.memory = Memory()
#         self.hard_drive = HardDrive()
#
#     def start(self):
#         self.cpu.freeze()
#         self.memory.load(0, 'boot_loader')
#         self.cpu.jump(0)
#         self.cpu.execute()
#
#     def shutdown(self):
#         pass
#
#
# computer = Computer()
# computer.start()
# computer.shutdown()


########################################################################################################################

"""Behavioral Design Pattern Implementation"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        ...


class Light:
    def on(self):
        print('Light is on')


    def off(self):
        print('Light is off')


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        if name in self.commands:
            self.commands[name].execute()

        else:
            print('Command is not found')


light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
RemoteControl.add_command('on', light_on_command)
RemoteControl.add_command('off', light_off_command)
