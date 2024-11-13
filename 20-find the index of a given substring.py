import pandas as pd
data = {'Names': ['Harini', 'Tejaswini', 'Sowmya', 'Meghana']}
df = pd.DataFrame(data)
substring = 'ni'
df['Index'] = df['Names'].str.find(substring)
print(df)
