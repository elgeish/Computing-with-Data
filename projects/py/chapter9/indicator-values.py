import numpy as np
import pandas as pd

data = [23, 13, 5, 3, 41, 33]
indicator_values = pd.get_dummies(pd.qcut(data, 2))
print("indicator_values:", indicator_values)
