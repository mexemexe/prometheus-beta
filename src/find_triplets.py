def find_triplets_with_sum(arr, target_sum):
    """
    Find all unique triplets in the array that sum up to the target sum.
    
    Args:
        arr (list): Input list of integers
        target_sum (int): Target sum to find triplets for
    
    Returns:
        list: List of unique triplets that sum up to target_sum
    
    Time Complexity: O(n^2)
    Space Complexity: O(1) excluding the output list
    
    Raises:
        TypeError: If input is not a list or target_sum is not an integer
        ValueError: If input list contains non-integer elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(target_sum, int):
        raise TypeError("Target sum must be an integer")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All array elements must be integers")
    
    # Sort the array to help with duplicate handling and two-pointer technique
    arr.sort()
    triplets = []
    n = len(arr)
    
    for i in range(n - 2):
        # Skip duplicates for the first element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # Use two-pointer technique to find the other two elements
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                # Found a triplet
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates for left and right
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif current_sum < target_sum:
                left += 1
            
            else:
                right -= 1
    
    return triplets