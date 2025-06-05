"""
Asymptotic complexity in terms of the number of elements in the array `n` :
* Time: O(n).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def insert_element_at_position(nums, element, position):

    # Insert the given element at the specified position (0-indexed).
    nums.insert(position-1, element)

    # Remove the last element from the list to maintain the original length.
    nums.pop()

    # Return the modified list.
    return nums

result_list = insert_element_at_position(nums=[2, 4, 5, 6, -1], element=40, position=4)
print(result_list)