#!/bin/bash

# Created  the Python script for the determinant function
cat > 0-determinant.py <<EOF
def determinant(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive Laplace expansion
    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(submatrix)
    return det
EOF

# Creating the main Python program to test the determinant function
cat > 0-main.py <<EOF
if __name__ == '__main__':
    determinant = __import__('0-determinant').determinant

    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))  # 1
    print(determinant(mat1))  # 5
    print(determinant(mat2))  # -2
    print(determinant(mat3))  # 0
    print(determinant(mat4))  # 192
    try:
        determinant(mat5)
    except Exception as e:
        print(e)  # matrix must be a list of lists
    try:
        determinant(mat6)
    except Exception as e:
        print(e)  # matrix must be a square matrix
EOF

# Execute the main Python program
python3 0-main.py

# Cleanup
rm 0-determinant.py 0-main.py
