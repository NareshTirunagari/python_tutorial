import numpy as np

arr3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
], dtype='int8')

#data type of the array
print(type(arr3))

#number of dimensions in the array
print(arr3.ndim)

#size of the array?
print(arr3.size)

#shape of the array
print(arr3.shape)

#data type of the elements
print(arr3.dtype)
