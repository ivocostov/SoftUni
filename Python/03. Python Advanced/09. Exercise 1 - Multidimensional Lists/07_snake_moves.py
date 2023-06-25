"""
Input:          |       Output:
                |
5 6             |       SoftUn
SoftUni         |       UtfoSi
                |       niSoft
---             |       foSinU
                |       tUniSo
1 4             |
Python          |
                |
"""

from collections import deque

rows, cols = [int(x) for x in input().split()]

user_string = list(input())                  # причината да се използва лист е защото ще се използва копие на думата
user_string_copy = deque(user_string)        # и ще се работи с queue

for row in range(rows):
    while len(user_string_copy) < cols:
        user_string_copy.extend(user_string)

    if row % 2 == 0:
        print(*[user_string_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[user_string_copy.popleft() for _ in range(cols)][::-1], sep='')


"""
You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M. 
A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end. 
The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
•	On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}". 
•	On the second line, you will receive the string representing the snake
Output
•	You should print the snake's zigzag path of size N x M (rows x columns)
Constraints
•	The dimensions N and M of the matrix will be integers in the range [1 … 12]
•	The snake will be a string with length in the range [1 … 20] and will not contain any whitespace characters

"""