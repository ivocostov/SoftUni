fuel_type = str(input())
fuel_liters = float(input())

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")

if fuel_type == "Diesel" and fuel_liters >= 25:
    print(f"You have enough {fuel_type.lower()}")
else:
    if fuel_type == "Diesel" and fuel_liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")

if fuel_type == "Gasoline" and fuel_liters >= 25:
    print(f"You have enough {fuel_type.lower()}.")
else:
    if fuel_type == "Gasoline" and fuel_liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")

if fuel_type == "Gas" and fuel_liters >= 25:
    print(f"You have enough {fuel_type.lower()}.")
else:
    if fuel_type == "Gas" and fuel_liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")



