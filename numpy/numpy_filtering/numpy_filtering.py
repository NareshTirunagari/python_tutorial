import numpy as np

#===========================================================
# 1-dimensional array
#------------------------------
arr = np.array([41, 42, 43, 44])
print(arr)


# 1. option1: manual filtering
#--------------------------------
filter_arr = [False, True, False, True]

print(filter_arr)

# printing true values only which means even numbers only
print(arr[filter_arr])


# 2. option2: create filter
#--------------------------------
filter_arr = []

for x in arr:
    if x % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)

# printing true values only which means even numbers only
print(arr[filter_arr])  


# 3. option3: shorter version
#--------------------------------
filter_arr = (arr % 2 == 0) # for each element in arr, it will check if even or odd and story True for even, False for odd.    

print(filter_arr)

# printing true values only which means even numbers only
print(arr[filter_arr])

#================================================================================
#===========================================================
# 2-dimensional array
#------------------------------

arr = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(arr)

filter_arr = (arr % 2 == 0)
print(filter_arr)
print(arr[filter_arr])

