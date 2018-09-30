import numpy as np
import pandas as pd

data = pd.DataFrame([[1, 2, np.nan],
                    [3, np.nan, 4],
                    [1, 2, 3]])

# Example 1 - the isnull method
print(f"data:\n{data}")
print("pd.isnull(data):")
print(pd.isnull(data))

# Example 2 - the dropna method
# Drop rows
print("data.dropna():")
print(data.dropna())
# Drop columns
print("data.dropna(axis = 1):")
print(data.dropna(axis = 1))

# Example 3 - the fillna method
# Fill in missing entries with column means
print("data.fillna(data.mean()):")
print(data.fillna(data.mean()))
