def read_matrix(filename: str, num_rows: int, num_cols: int) -> list[list[int]]:
    """
    Reads a matrix from a file and returns it as a 2D list of integers.

    Parameters:
    filename (str): The name of the file containing the matrix.
    num_rows (int): The number of rows in the matrix.
    num_cols (int): The number of columns in the matrix.

    Returns:
    list[list[int]]: A 2D list (matrix) where each element is an integer.
    
    The file contains the matrix elements separated by spaces, one row per line.
    """

print(read_matrix("matrix.txt", 3, 3))