# i= 1
# while i<= 4: # outterloop
#     j = 1   # varible
#     while j<=2: # inner loop
#         print(f"i={i}, j={j}")
#         j +=1 # inner loop iteration
#     i +=1 # outerLoop iteration
    
# i= 1
# while i<= 2: # outterloop
#     j = 1   # varible
#     while j<=2: # inner loop
#         print(f"i={i}, j={j}")
#         j *=2 # inner loop iteration
#     i *=2 # outerLoop iteration
 
 # 2D matrix
# matrix =[
#      [1, 2, 3],
#      [3, 4, 5],
#      [7, 8, 9],
# ]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for element in row:
#         print(element*2, end=" ")
#     print()

# matrix = [
#     [2, 4, 6],
#     [8, 10, 12],
#     [14, 16, 18]
# ]
# for row in matrix:
#     for element in row:
#         print(int(element/2), end=" ")
#     print()

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# # acessing by index
# for i in range(len(matrix)):          
#     for j in range(len(matrix[i])):   
#         print(f"matrix[{i}][{j}] = {matrix[i][j]}")

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

#grid format
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print(" | ".join(str(x) for x in row))

# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] *= 2 

# print(matrix)