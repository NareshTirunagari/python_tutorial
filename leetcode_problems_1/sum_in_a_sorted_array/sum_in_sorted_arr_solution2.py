"""
# Given an array sorted in non-decreasing order and a target number, 
# find the indices of the two values from the array that sum up to the given target number.

Example
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output:

[1, 3]
Sum of the elements at index 1 and 3 is 7.

Notes
In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the indices returned does not matter.
A single index cannot be used twice.
Constraints:

2 <= array size <= 105
-105 <= array elements <= 105
-105 <= target number <= 105
Array can contain duplicate elements.
"""

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    numbers_dict = {} #story number as key and its index as value
    #for each number in the list
    for index, current in enumerate(numbers):
        required = target - current # complementary target pair

        if required in numbers_dict: #is pair found??
            return[index, numbers_dict[required]] #return the pair's indices
        else:
            numbers_dict[current] = index #store the current number and its index
    
    # If no pair sums up to the target, return [-1, -1]
    return [-1, -1]

print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=13))
print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=77))

input_data = {
    "numbers": [1, 4, 13, 15, 20],
    "target": 21
}
print(pair_sum_sorted_array(input_data["numbers"], input_data["target"]))
