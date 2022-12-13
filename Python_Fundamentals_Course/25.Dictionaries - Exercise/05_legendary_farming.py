legendary_farming = {"shards": 0, "fragments": 0, "motes": 0}

item_is_obtained = False

gamer_input = input().split()
while not item_is_obtained:

    for index in range(0, len(gamer_input), 2):
        value = int(gamer_input[index])
        key = gamer_input[index + 1].lower()

        if key not in legendary_farming.keys():
            legendary_farming[key] = 0
        legendary_farming[key] += value

        if legendary_farming["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_farming["shards"] -= 250
            item_is_obtained = True
        elif legendary_farming["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_farming["fragments"] -= 250
            item_is_obtained = True
        elif legendary_farming["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_farming["motes"] -= 250
            item_is_obtained = True

        if item_is_obtained:
            break
    if item_is_obtained:
        break

    gamer_input = input().split()

for material, quantity in legendary_farming.items():
    print(f"{material}: {quantity}")
