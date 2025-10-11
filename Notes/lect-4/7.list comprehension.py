# list comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# flat = [num for row in matrix for num in row]
# print(flat)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# flat =[]
    
# for row in matrix:
#     for num in row:
#         flat.append(matrix)
# print(flat)


# flat =[]
# for row in matrix:
#     for num in row:
#         flat.append(num)
# print (flat)

#multiply each element by 2
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# doubled = [[num * 2 for num in row] for row in matrix]
# print(doubled)

# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# doubled = [[num * 4 for num in row] for row in matrix]
# print(doubled)

# matrix = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#  ]
# doubled = [[num * 4 for num in row] for row in matrix]
# print(doubled)

# zeros = [[0 for _ in range(4)] for _ in range(4)]
# print(zeros)

# one = [[1 for _ in range(2)] for _ in range(3)]
# print(one)

matrix = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

odd = [num for row in matrix for num in row if num%2 !=0]
print(odd)