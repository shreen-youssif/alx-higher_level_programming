def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by the divisor.

    Raises:
        TypeError: If the input matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is equal to 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
