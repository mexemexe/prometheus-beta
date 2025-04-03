def bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    Args:
        arr (list): Input list of comparable elements to be sorted.
    
    Returns:
        list: Sorted list in ascending order.
    
    Raises:
        TypeError: If input is not a list.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    n = len(arr)
    for i in range(n):
        # Flag to optimize: If no swaps occur, array is already sorted
        swapped = False
        
        # Reduce iterations by comparing only unsorted portion
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr