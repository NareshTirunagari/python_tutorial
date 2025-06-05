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
    # Initialize two pointers, one at the start of the list and one at the end.
    start = 0
    end = len(nums) - 1

    # Continue until the two pointers meet in the middle.
    while start < end:
        # Swap the elements at the positions of the two pointers.
        nums[start], nums[end] = nums[end], nums[start]

        # Move the start pointer one step forward and the end pointer one step backward.
        start += 1
        end -= 1

    # Return the reversed list.
    return nums

# Define a list and call the function
result_list = reverse_array(nums=[34, 56, 21, 14, 71, 19, 9, 62])
print(result_list)
