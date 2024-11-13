import pandas as pd
import matplotlib.pyplot as plt

# Sample data with more dates
data = {'Date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05', '2024-10-06', '2024-10-07', '2024-10-08'],
        'Volume': [1250000, 1300000, 1350000, 1400000, 1450000, 1500000, 1550000, 1600000],
        'Stock_Price': [2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100]}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter by date range
filtered_df = df[(df['Date'] >= '2024-10-03') & (df['Date'] <= '2024-10-07')]

# Scatter plot
plt.scatter(filtered_df['Volume'], filtered_df['Stock_Price'])
plt.show()
