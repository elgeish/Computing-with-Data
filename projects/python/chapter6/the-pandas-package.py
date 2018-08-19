import pandas as pd
import numpy as np

# Example: how to create a dataframe
data = {
  "names": ["John", "Jane", "George"], 
  "age": [25, 35, 52],
  "height": [68.1, 62.5, 60.5],
}
df = pd.DataFrame(data)
print("dataframe content =\n" + str(df))
print("dataframe types =\n" + str(df.dtypes))

# Example: accessing data in a data frame
df["age"] = 35  # assign 35 to all age values
print("age column =\n" + str(df["age"]))
print("height column =\n" + str(df.height))
print("second row =\n" + str(df.ix[1]))

# Example: adding a new column
df = pd.DataFrame(data)
df["weight"] = [170.2, 160.7, 185.5]
print(df)

# Example: the median function
df = pd.DataFrame(data)
print("medians of columns =\n" + str(df.median()))
print("medians of rows =\n" + str(df.median(axis=1)))

# Example: apply f(x) = x + 1 to all columns
data = {
  "age": [25.2, 35.4, 52.1],
  "height": [68.1, 62.5, 60.5],
  "weight": [170.2, 160.7, 185.5],
}
df = pd.DataFrame(data)
print(df.apply(lambda z: z + 1))

# Example: working with missing data
data = {
  "age" : [25.2, np.nan, np.nan],
  "height" : [68.1, 62.5, 60.5],
  "weight" : [170.2, np.nan, 185.5],
}
df = pd.DataFrame(data)
# NA stands for Not Available
print("column means (NA skipped):")
print(str(df.mean()))
print("column means: (NA not skipped)")
print(str(df.mean(skipna=False)))
