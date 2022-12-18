climbers_group = int(input())

mussala_climbers = 0
monblanc_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for num in range(1, climbers_group + 1):
    group_members_qty = int(input())
    total_climbers += group_members_qty
    if group_members_qty <= 5:
        mussala_climbers += group_members_qty
    elif group_members_qty <= 12:
        monblanc_climbers += group_members_qty
    elif group_members_qty <= 25:
        kilimandjaro_climbers += group_members_qty
    elif group_members_qty <= 40:
        k2_climbers += group_members_qty
    else:
        everest_climbers += group_members_qty

mussala_climbers_percentage = mussala_climbers / total_climbers * 100
monblanc_climbers_percentage = monblanc_climbers / total_climbers * 100
kilimandjaro_climbers_percentage = kilimandjaro_climbers / total_climbers * 100
k2_climbers_percentage = k2_climbers / total_climbers * 100
everest_climbers_percentage = everest_climbers / total_climbers * 100

print(f"{mussala_climbers_percentage:.2f}%")
print(f"{monblanc_climbers_percentage:.2f}%")
print(f"{kilimandjaro_climbers_percentage:.2f}%")
print(f"{k2_climbers_percentage:.2f}%")
print(f"{everest_climbers_percentage:.2f}%")
