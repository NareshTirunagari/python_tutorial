import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(2, 6)
print('\nReshaped into 2 by 6 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)

new_arr = arr.reshape(3, 4)
print('\nReshaped into 3 by 4 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)

new_arr = arr.reshape(4, 3)
print('\nReshaped into 4 by 3 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)

new_arr = arr.reshape(6, 2)
print('\nReshaped into 6 by 2 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)

new_arr = arr.reshape(2, 2, 3)
print('\nReshaped into 2 by 2 by 3 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)

new_arr = arr.reshape(2, 3, 2)
print('\nReshaped into 2 by 3 by 2 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)


new_arr = arr.reshape(3, 2, 2)
print('\nReshaped into 3 by 2 by 2 array:\n\n',new_arr)
print('\nDimension of the new array:', new_arr.ndim)