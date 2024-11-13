import pandas as pd
data = {'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Sale_Value': [100, 200, 150, 50, 250, 30]}
df = pd.DataFrame(data)
# Create Pivot Table
pivot_table = pd.pivot_table(df, values='Sale_Value', index='Item', aggfunc=['max', 'min'])
print(pivot_table)
