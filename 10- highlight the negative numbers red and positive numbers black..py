import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Create a plot to display the table
fig, ax = plt.subplots(figsize=(8, 4))  # Set the size of the plot
ax.axis('off')  # Hide the axes

# Create a color map for negative and positive values
colors = df.applymap(lambda x: 'red' if x < 0 else 'black')

# Render the table with red for negative values and black for positive
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Apply color to each cell in the table
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        table[(i, j)].set_text_props(color=colors.iloc[i, j])

# Display the plot
plt.show()
