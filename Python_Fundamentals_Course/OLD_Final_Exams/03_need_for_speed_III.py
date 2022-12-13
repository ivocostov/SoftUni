def initial_dictionary(number_of_cars):
    for cars in range(number_of_cars):
        car_models = input().split("|")
        car = car_models[0]
        mileage = int(car_models[1])
        fuel = int(car_models[2])
        cars_dictionary[car] = [mileage, fuel]


def drive(car, distance, fuel):
    if car in cars_dictionary.keys():
        if fuel > int(cars_dictionary[car][1]):
            print("Not enough fuel to make that ride")
        else:
            cars_dictionary[car][0] += distance
            cars_dictionary[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if int(cars_dictionary[car][0]) >= 100000:
            del cars_dictionary[car]
            print(f"Time to sell the {car}!")


def refuel(car, fuel):
    if car in cars_dictionary.keys():
        if int(cars_dictionary[car][1]) < 75:
            tank_available_space = 75 - int(cars_dictionary[car][1])
            if fuel > tank_available_space:
                fuel = tank_available_space
                cars_dictionary[car][1] += fuel
            else:
                cars_dictionary[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")


def revert(car, kilometers):
    if car in cars_dictionary.keys():
        cars_dictionary[car][0] -= kilometers

        if cars_dictionary[car][0] <= 10000:
            cars_dictionary[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")


def main_function(number_of_cars):
    initial_dictionary(number_of_cars)

    while True:
        command = input().split(' : ')
        if command[0] == 'Stop':
            break

        action = command[0]
        if action == 'Drive':
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            drive(car, distance, fuel)
        elif action == 'Refuel':
            car = command[1]
            fuel = int(command[2])
            refuel(car, fuel)
        elif action == 'Revert':
            car = command[1]
            kilometers = int(command[2])
            revert(car, kilometers)

    for cars, values in cars_dictionary.items():
        print(f"{cars} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.")


cars_count = int(input())
cars_dictionary = {}
main_function(cars_count)