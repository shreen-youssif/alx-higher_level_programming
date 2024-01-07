def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                    or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty, not a rectangle,
                    or cannot be multiplied.
    """

    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))

        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))

        if not matrix or any(not row for row in matrix):
            raise ValueError("{} can't be empty".format(name))

        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError("{} should contain only integers or floats".format(name))

        if len(set(len(row) for row in matrix)) > 1:
            raise TypeError("Each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = [[sum(a * b for a, b in zip(row_a, col_b))
                        for col_b in zip(*m_b)] for row_a in m_a]

    return result_matrix
