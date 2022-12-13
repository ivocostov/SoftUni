food_qty_in_kg = float(input())
hay_qty_in_kg = float(input())
cover_qty_in_kg = float(input())
guinea_weight_in_kg = float(input())

food_in_grams = food_qty_in_kg * 1000
hay_in_grams = hay_qty_in_kg * 1000
cover_in_grams = cover_qty_in_kg * 1000
guinea_weight_in_grams = guinea_weight_in_kg * 1000


for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0:
        cover_in_grams -= guinea_weight_in_grams / 3

food_qty_in_kg = food_in_grams / 1000
hay_qty_in_kg = hay_in_grams / 1000
cover_qty_in_kg = cover_in_grams / 1000

if food_qty_in_kg > 0 and hay_qty_in_kg > 0 and cover_qty_in_kg > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_qty_in_kg:.2f}, Hay: {hay_qty_in_kg:.2f}, "
          f"Cover: {cover_qty_in_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
