import numpy as np

# 1-d array
arr = np.array([1, 2, 3])

for x in arr:
    print(x, end=' ')


# 2-d array
arr = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6]
    ]
)
print('\nPrint dimension by dimension:')
for x in arr:
    print(x, end=' ')


print('\nPrint all elements:')
for x in arr:
    for value in x:
        print(value, end=' ')
