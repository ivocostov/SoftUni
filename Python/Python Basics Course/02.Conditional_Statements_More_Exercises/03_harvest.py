from math import ceil, floor
vineyard_area_sqm = int(input())
grapes_kg_per_sqm = float(input())
wine_lt_for_sale = int(input())
workers_qty = int(input())

total_grapes_kg = vineyard_area_sqm * grapes_kg_per_sqm
grapes_for_wine = total_grapes_kg * 0.4
produced_wine_in_liters = grapes_for_wine / 2.5
wine_qty_difference_in_lt = abs(wine_lt_for_sale - produced_wine_in_liters)
wine_per_worker = wine_qty_difference_in_lt / workers_qty

if produced_wine_in_liters >= wine_lt_for_sale:
    print(f"Good harvest this year! Total wine: {floor(produced_wine_in_liters)} liters.")
    print(f"{ceil(wine_qty_difference_in_lt)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(wine_qty_difference_in_lt)} liters wine needed.")
