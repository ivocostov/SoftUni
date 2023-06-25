def sorting_cheeses(**cheeses):
    sorted_cheeses = sorted(cheeses.items(), key=lambda n: (-len(n[1]), n[0]))

    end_list = []

    for cheese, quantity in sorted_cheeses:
        end_list.append(cheese)
        end_list.extend(quantity)

    return '\n'.join(str(el) for el in end_list)


# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
