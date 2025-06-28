import pandas as pd

df = pd.read_csv('python_tutorial\data\examples.csv')
print('\n\nprinting df data:\n')
print(df)
print('\n\nprinting df info:\n')
print(df.info())
print('\n\nprinting df description:\n')
print(df.describe())

print('\n')
print(df.head(n=3))

print('\n')
print(df.tail(n=2))

print('\nshape:')
print(df.shape)

print('\n columns:')
print(df.columns)

print('\n list of columns:')
print(list(df.columns))
