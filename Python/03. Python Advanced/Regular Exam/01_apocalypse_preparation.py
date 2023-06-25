from collections import deque


textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

healing_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}


def apocalypse_preparation(textiles, medicaments):

    while textiles and medicaments:

        current_textile = textiles.popleft()
        current_medicament = medicaments.pop()
        combined_ingredients = current_textile + current_medicament

        for item, resource in (('Patch', 30), ('Bandage', 40), ('MedKit', 100)):
            if combined_ingredients == resource:
                healing_items[item] += 1
                break

            elif combined_ingredients > 100:
                healing_items['MedKit'] += 1
                next_medicament = medicaments.pop()
                next_medicament += combined_ingredients - 100
                medicaments.append(next_medicament)
                break

        else:
            current_medicament += 10
            medicaments.append(current_medicament)

    if not textiles and medicaments:
        print("Textiles are empty.")
    elif textiles and not medicaments:
        print("Medicaments are empty.")
    elif not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")

    sorted_data = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

    for element, quantity in sorted_data:
        if quantity != 0:
            print(f"{element} - {quantity}")


    if textiles:
        #sorted_list_of_textiles = sorted([x for x in textiles], reverse=True)
        #print(f"Textiles left: {', '.join(map(str, sorted_list_of_textiles))}")
        print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
    if medicaments:
        sorted_list_of_medicaments = sorted([x for x in medicaments], reverse=True)
        print(f"Medicaments left: {', '.join(map(str, sorted_list_of_medicaments))}")


apocalypse_preparation(textiles, medicaments)