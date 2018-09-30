import numpy as np
import pandas as pd

# Example 1 - concatenate two dataframes
data1 = {"ID" : ["2134", "4524"],
         "name" : ["John Smith", "Jane Doe"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["9423", "3483"],
         "name" : ["Bob Jones", "Mary Smith"]}
df2 = pd.DataFrame(data2)
df3 = pd.concat([df1, df2])
print("concatenation of df1 and df2:\n" + str(df3))

# Example 2 - concatenating dataframes with non identical columns
data1 = {"ID" : ["2134", "4524"],
         "name" : ["John Smith", "Jane Doe"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["9423", "3483"],
         "nick name" : ["Bobby", "Abby"]}
df2 = pd.DataFrame(data2)
df3 = pd.concat([df1, df2])
print("concatenation of df1 and df2:\n" + str(df3))

# Example 3 - inner join
data1 = {"ID" : ["2134", "4524"],
         "name" : ["John Smith", "Jane Doe"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["6325", "2134"],
         "age" : [25, 35],
         "tenure" : [3, 8]}
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on = 'ID', how = 'inner')
print("inner join of df1 and df2:\n" + str(df3))

# Example 3 - outer and left joins
data1 = {"ID" : ["2134", "4524"],
         "name" : ["John Smith", "Jane Doe"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["6325", "2134"],
         "age" : [25, 35],
         "tenure" : [3, 8]}
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on = 'ID', how = 'outer')
print("outer join of df1 and df2:\n" + str(df3))
df4 = pd.merge(df1, df2, on = 'ID', how = 'left')
print("left join of df1 and df2:\n" + str(df4))

# Example 4 - outer join with multiple records with the same key
data1 = {"ID" : ["2134", "4524", "2134"],
         "name" : ["John Smith", "Jane Doe", "JOHN SMITH"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["6325", "2134"],
         "age" : [25, 35],
         "tenure" : [3, 8]}
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on = 'ID', how = 'outer')
print("outer join of df1 and df2:\n" + str(df3))

# Example 5 - outer join with attribute name suffix
data1 = {"ID" : ["2134", "4524"],
         "f1" : ["John Smith", "Jane Doe"]}
df1 = pd.DataFrame(data1)
data2 = {"ID" : ["6325", "2134"],
         "f1" : [25, 35],
         "f2" : [3, 8]}
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on = 'ID', how = 'outer')
print("outer join of df1 and df2:\n" + str(df3))
