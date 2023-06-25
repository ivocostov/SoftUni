# single dimensional list
my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list)
my_list.append(-11)
print(my_list)
my_list.pop()
print(my_list)

# multi - dimensional list or
# list of lists

multi_dim_list = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]

print(multi_dim_list)
multi_dim_list.append([-11])  # тук се добавя лист, защото са листове в лист
print(multi_dim_list)
multi_dim_list.pop()
print(multi_dim_list)

# достъп до елементите във вложените листи

print(multi_dim_list[1])

three_dim_list = [
    [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]

    ],

    [
        [4, 5, 6],
        [5, 6, 7],
        [5, 7, 8]
    ],

    [
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11]
    ]

]

#  matrix_demos

ll = []
n = 10

for _ in range(n):
    ll.append(0)
