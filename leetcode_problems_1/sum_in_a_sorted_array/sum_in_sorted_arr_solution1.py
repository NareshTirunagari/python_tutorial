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

    # Set up two pointers: 'start' at the beginning of the array and 'end' at the end of the array
    start, end = 0, len(numbers) - 1

    # While the 'start' pointer is less than the 'end' pointer
    while start < end:

        # Calculate the current sum of the values pointed by the 'start' and 'end' pointers
        temp_sum = numbers[start] + numbers[end]
        if(temp_sum == target): # if the current sum is exactly equal to the target then return
            return [start, end] # Return the indices of the two numbers that add up to the target
        elif(temp_sum < target): # If the current sum is less than the target
            start += 1 # Move the 'start' pointer one step towards the end
        else: #Else if the current sum is more than the target
            end -= 1 # Move the 'end' pointer one step towards the start

    # If no pair sums up to the target, return [-1, -1]
    return [-1, -1]

print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=7))
print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=77))
