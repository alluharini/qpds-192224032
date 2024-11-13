import pandas as pd
data = {'Names': ['Harini', 'Tejaswini', 'Sowmya', 'Meghana']}
df = pd.DataFrame(data)
df['Names'] = df['Names'].str.swapcase()
print(df)
