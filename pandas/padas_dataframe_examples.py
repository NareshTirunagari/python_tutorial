import pandas as pd

df = pd.read_csv('python_tutorial\data\examples.csv')
print('\n\nprinting df data:\n')
print(df)
print('\n\nprinting df info:\n')
print(df.info())
print('\n\nprinting df description:\n')
print(df.describe())