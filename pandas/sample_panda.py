import pandas as pd

#create panda series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print(series)
print()
print(type(series))

series = pd.Series(
    [10, 20, 30, 40],
    index = ['A', 'B', 'C', 'D']
)

series['E'] = 50
print(series)

