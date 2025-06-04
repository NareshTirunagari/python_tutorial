def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    # return nums[::-1]  ##this will also work  
    return nums[-1::-1]


# Define a list and call the function
result_list = reverse_array(nums=[34, 56, 21, 14, 71, 19, 9, 62])
print(result_list)
