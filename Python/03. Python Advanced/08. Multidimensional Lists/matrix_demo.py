''' Create list of n count of '0' '''

# my_list = []
# n = 5
#
# for _ in range(n):
#     my_list.append(0)
#
# print(my_list)

''' Create matrix of NxM count of '0' '''

n = 5
m = 7

mm = []
for _ in range(n):
    ll = []
    for _ in range(m):
        ll.append(0)

    mm.append(ll)

# Ако искаме да добавим поредни числа в списъка:

n = 5
m = 7

mm = []
for _ in range(n):
    ll = []
    for i in range(m):   # добавя текущия индекс в списъка, като поредно число
        ll.append(i)

    mm.append(ll)

''' Create matrix with comprehension '''

ll = [1, 2, 3, 4, 5, 6, 7]
ll2 = []

for v in ll:
    ll2.append(v + 1)

print(ll)
print(ll2)

ll3 = [v + 1 for v in ll]
print(ll3)

# if we have a matrix:

mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(mm)

print(
    [[v + 1 for v in row] for row in mm]
)

''' Nested comprehension or a new list for each list in multidimensional list '''


print(
    # MD comprehension
    # Flattening comprehension
    [
        v + 1
        for row in mm           # за всеки ред от матрицата и вземи стойност
            for v in row
    ]
)

matrix = [[x for x in row] for row in input()]