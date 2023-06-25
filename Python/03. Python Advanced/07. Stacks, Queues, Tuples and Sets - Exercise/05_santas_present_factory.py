from collections import deque

value_of_materials = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())

presents = []

santas_presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while value_of_materials and magic_values:
    current_material = value_of_materials.pop() if magic_values[0] or not value_of_materials[0] else 0
    current_magic = magic_values.popleft() if current_material or not magic_values[0] else 0

    if not current_magic:
        continue

    result = current_material * current_magic

    if santas_presents.get(result):
        presents.append(santas_presents[result])
    elif result < 0:
        value_of_materials.append(current_material + current_magic)
    elif result > 0:
        value_of_materials.append(current_material + 15)

if {"Doll", "Wooden train"}.issubset(presents) or {"Teddy bear", "Bicycle"}.issubset(presents):  # къдравите скоби са сетове не речници
    print(f"The presents are crafted! Merry Christmas!")                                         # за да може да се използва issubset
else:
    print("No presents this Christmas!")
if value_of_materials:
    print(f"Materials left: {', '.join([str(x) for x in value_of_materials][::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

[print(f"{toy}: {presents.count(toy)}") for toy in sorted(set(presents))]
