"""
Asymptotic complexity in terms of length of the given list `n`:
* Time: O(n).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def reverse_array(nums):
    """
    Args:
     nums(list_int32): A list of integers.
    Returns:
     list_int32: The reversed list of integers.
    """
    # Reverse the order of elements in the list.
    nums.reverse()

    # Return the modified (reversed) list.
    return nums

# Define a list and call the function
result_list = reverse_array(nums=[34, 56, 21, 14, 71, 19, 9, 62])
print(result_list)
