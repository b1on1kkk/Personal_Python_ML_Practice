import numpy as np
import pandas as pd
import os


# create test and small dataframe
# np.random.seed(101)
# data = np.random.randint(0, 101, (4, 3))
# index = ['CA', 'NY', 'AZ', 'TX']
# columns = ['Jan', 'Feb', 'Mar']
#
# df = pd.DataFrame(data, index, columns)

df = pd.read_csv('data.csv')

print(df)