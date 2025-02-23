# 2D list
matrix = [[1, 2, 3], [3, 4, 5], [4, 5, 6]]
print(matrix[0]) # Use one bracket to access a row.
print(matrix[0][2]) # Use one bracket to access individual number in the matrix.
# With the same method above, we can also modify the individual number in the matrix.
matrix[1][1] = 5 # Here we change from 4 to 5.
print(matrix[1])
for row in matrix:
    print(row) # To display each row.
for row in matrix:
    for item in row:
        print(item) # To display individual item in the matrix.