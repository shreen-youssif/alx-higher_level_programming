import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
            The result of multiplying m_a and m_b.

    Raises:
        ValueError: If m_a or m_b is empty,
                    not a rectangle, or cannot be multiplied.
    """


    np_a = np.array(m_a)
    np_b = np.array(m_b)

    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = np.matmul(np_a, np_b)

    return result_matrix
