import pandas as pd

def print_file(file_name):
  with open(file_name) as f:
    for line in f:
      print(line, end='')

data_frame = pd.DataFrame({
  "age": [25.2, 35.4, 52.1],
  "height": [68.1, 62.5, 60.5],
  "weight": [170.2, 160.7, 185.5],
})
file_name = "dataframe.csv"
data_frame.to_csv(file_name, index=False)
loaded = pd.read_csv(file_name)
print("Data Frame:\n{}".format(loaded))
print("Text File Content:")
print_file(file_name)
