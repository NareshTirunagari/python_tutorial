import numpy as np

arr = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)

print(arr)

#get the 2nd element on the 1st row
print(arr[0, 1])
print(arr[0][1])

#get the 5th element on the 2nd row
print(arr[1,4])
print(arr[1][4])
print(arr[1, -1])
print(arr[1][-1])

#get the first 3 elements on the 2nd row
print(arr[1, :3])
print(arr[1, 0:3])
print(arr[1][0:3])
print(arr[1][:3])


arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

#print element 1 to 4
print(arr1[1:5])

print(arr1[4:])

print(arr1[:4])

print(arr1[-3:-1])

print(arr1[1:5:2])

#print all the elements by jumping 2 steps means ignore 2nd element, 4th element, 6th element etc
print(arr1[::2]) 
