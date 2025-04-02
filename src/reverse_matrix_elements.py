def reverse_matrix_elements(matrix):
    """
    Reverses each element in the given matrix.

    Args:
        matrix (List[List[int]]): A square matrix of integers
            with size between 1 and 1000.

    Returns:
        List[List[int]]: A new matrix with each element reversed.

    Raises:
        ValueError: If the matrix is not square or size is invalid.
    """
    # Validate matrix is square
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square and non-empty")

    # Validate matrix size
    n = len(matrix)
    if n < 1 or n > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")

    # Create new matrix with reversed elements
    reversed_matrix = [
        [int(str(abs(elem))[::-1]) for elem in row]
        for row in matrix
    ]

    return reversed_matrix