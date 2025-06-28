import numpy as np

arr = np.array(
    [
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [10,11,12]
        ]
    ]
)

print('\nDimension of the new array:', arr.ndim)

print('\nPrint dimension by dimension:')
for value in arr:
    print(value, end=' ')

print('\n\nPrint all elements:')
for value in arr:
    for x in value:
        print(value, end=' ')



print('\n\nPrint without using nested for loops:')
for index, value in np.ndenumerate(arr):
    print(index, value)