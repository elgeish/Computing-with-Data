# Example 1 - binning
import numpy as np
import pandas as pd

data = [23, 13, 5, 3, 41, 33]
bin_boundaries = [0, 10, 20, 30, 40, 50]
bin_values = [5, 15, 25, 35, 45]
cut_data = pd.cut(data, bin_boundaries)
print("labels:", cut_data.codes)
binned_data = np.zeros(shape = np.size(data))
for k, x in enumerate(cut_data.codes):
    binned_data[k] = bin_values[x]
print("binned_data:", binned_data)

# Example 2 - quantile binning
original_data = [23, 13, 5, 3, 41, 33]
cut_data = pd.qcut(original_data, 2)
print("C.labels:", cut_data.codes)
