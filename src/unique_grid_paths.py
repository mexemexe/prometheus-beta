def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or not a valid 2D list
    
    Time Complexity: O(T*R), where T is number of rows and R is number of columns
    Space Complexity: O(1)
    """
    # Check for empty or invalid matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Validate matrix structure 
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("All rows must have the same length")
    
    # Linear search through the entire matrix
    for row in matrix:
        for cell in row:
            if cell == target:
                return True
    
    return False