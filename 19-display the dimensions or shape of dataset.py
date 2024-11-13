import pandas as pd
df = pd.DataFrame({
    'Year': [1984, 1985, 1986, 1987, 1988],
    'Country': ['USA', 'Canada', 'France', 'Germany', 'Italy'],
    'Beverage Type': ['Beer', 'Wine', 'Beer', 'Spirits', 'Wine'],
    'Consumption': [10.5, 8.2, 11.7, 9.8, 7.5]
})
print("Dimensions of the dataset (rows, columns):", df.shape)
print("Column names in the dataset:")
print(df.columns.tolist())
