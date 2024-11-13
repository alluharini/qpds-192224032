import pandas as pd
data = {'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Units_Sold': [10, 20, 15, 5, 25, 3]}

df = pd.DataFrame(data)
# Create Pivot Table
pivot_table = pd.pivot_table(df, values='Units_Sold', index='Item', aggfunc='sum')

print(pivot_table)
