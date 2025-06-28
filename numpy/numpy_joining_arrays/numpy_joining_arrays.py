import numpy as np

#joining 1-dim arrays
arr1 = np.array([1, 2, 3])
arr2 = np. array([4, 5, 6])
print(arr1)
print()
print(arr2)
print()
arr3 = np.concatenate([arr1, arr2])
print(arr3)
print()
print()

#joining n-dim arrays

arr1 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

arr2 = np.array(
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
)

print(arr1)
print()
print(arr2)
print()

#joining vertically
arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)
print()

#joining horizontally
arr3 = np.concatenate([arr1, arr2], axis=1)
print(arr3)
print()

