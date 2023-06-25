from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey_qty = 0

hive = {
    '+': lambda bee, honey_qty: bee + honey_qty,
    '-': lambda bee, honey_qty: bee - honey_qty,
    '*': lambda bee, honey_qty: bee * honey_qty,
    '/': lambda bee, honey_qty: bee / honey_qty
}

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar_qty = nectar.pop()

    if current_nectar_qty >= current_bee:
        current_symbol = symbols.popleft()
        result = abs(hive[current_symbol](current_bee, current_nectar_qty))
        total_honey_qty += result

    elif current_nectar_qty <= current_bee:
        working_bees.appendleft(current_bee)


print(f"Total honey made: {total_honey_qty}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
