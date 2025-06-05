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
    # Iterate over each number in the list
    n = len(numbers)
    ##caution: This solution may timeout for very big lists.
    for i in range(n): #outer loop
        # For each number of the above outer loop, iterate over the rest of the numbers (exclude outer loop number) in the list
        for j in range(i+1, n): #inner loop
            # If the two numbers add up to the target, return their indices
            if(numbers[i] + numbers[j] == target):
                return[i, j]            

    # If no pair sums up to the target, return [-1, -1]
    return[-1, -1]

print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=13))
print(pair_sum_sorted_array(numbers=[1, 2, 3, 5, 10], target=77))
