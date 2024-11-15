import numpy as np
import pandas as pd

# Create DataFrame with random values and some NaNs
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
nan_indices = [(0, 2), (4, 1), (4, 3), (6, 4), (9, 4)]
for row, col in nan_indices:
    df.iat[row, col] = np.nan

# Keep rows with at least 2 NaN values
df_filtered = df[df.isna().sum(axis=1) >= 2]

# Display the filtered DataFrame
print(df_filtered)
