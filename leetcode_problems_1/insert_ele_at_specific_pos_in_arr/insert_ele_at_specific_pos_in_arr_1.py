def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    begin = len(nums) - 1
    tillPosition = position - 1
    jumpBackwards = -1
    
    for i in range(begin, tillPosition, jumpBackwards):
        nums[i] = nums[i-1]
        
    nums[tillPosition] = element
    return nums


result_list = insert_element_at_position(nums=[2, 4, 5, 6, -1], element=40, position=4)
print(result_list)

