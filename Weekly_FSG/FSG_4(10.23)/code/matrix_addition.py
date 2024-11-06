# Python that performs matrix addition

def matrix_addition(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    """
    Perform element-wise addition of two matrices m1 and m2.
    
    Parameters:
    m1 (list[list[int]]): First matrix.
    m2 (list[list[int]]): Second matrix.
    
    Returns:
    list[list[int]]: The resulting matrix after addition.
    """
    num_rows = len(m1) #2
    num_cols = len(m1[0]) #3
    # range
    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            addition = m1[i][j] + m2[i][j]
            row.append(addition)
        # row [8, 10, 12]
        matrix.append(row)
    return matrix

matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8, 9],
           [10,11,12]]
m = matrix_addition(matrix1, matrix2)
print(m, matrix1, sep="\n")