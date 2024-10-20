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

matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8, 9],
           [10,11,12]]
print(matrix_addition(matrix1, matrix2))