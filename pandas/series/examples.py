import numpy as np
import pandas as pd

# create kind of table #

# USA       |   1776
# Canada    |   1867
# Mexico    |   1821

# where ['USA', 'Canada', 'Mexico'] - indexes and dates are values

# index = ['USA', 'Canada', 'Mexico']
# independenceDates = [1776, 1867, 1821]
#
# ser = pd.Series(independenceDates, index)

# from table above you can get data as in typical dictionary:
# ser['USA'] -> will return 1776. and by parity of reasoning


# create Series table using dictionary #

# dictAges = {'Sam': 7, 'Mike': 5, 'Spike': 10}
# ser = pd.Series(dictAges)


# prepare data to generate Series
# keys_1 = ['Japan', 'China', 'India', 'USA']
# values_1 = np.random.randint(0, 300, size=4)
#
# keys_2 = ['Brazil', 'China', 'India', 'USA']
# values_2 = np.random.randint(0, 300, size=4)
#
#
# # function to generate Series
# def dictionary_creation(keys: list[str], values: np.ndarray):
#     return pd.Series(values, keys)
#
#
# q1 = dictionary_creation(keys_1, values_1)
# q2 = dictionary_creation(keys_2, values_2)
#
# # add data from q1 to q2 and if key is not exist in one of them fill it with 0
# print(q1.add(q2, fill_value=0))
