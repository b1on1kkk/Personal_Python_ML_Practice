import numpy as np
import pandas as pd

# more practice here:
# https://www.w3resource.com/python-exercises/pandas/index-data-series.php


# 1
# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using
# Pandas module.

# Solution
# arr = np.arange(0, 10)
# print(pd.Series(arr))


# 2
# Write a Pandas program to compare the elements of the two Pandas Series.

# Solution
# ser_1 = pd.Series([2, 4, 6, 8, 10])
# ser_2 = pd.Series([1, 3, 5, 7, 10])
# print(ser_1 > ser_2)


# 3
# Write a Pandas program to convert a dictionary to a Pandas series.

# Solution
# dictionary = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# print(pd.Series(dictionary))


# 4
# Write a Pandas program to change the data type of given a column or a Series.

# Solution
# before = pd.Series([100, 200, 'python', 300.12, 400])
# after = pd.to_numeric(before, errors='coerce')


# 5
# Write a Pandas program to change the data type of given a column or a Series.

# Solution
# frame = {'col1': np.random.randint(1, 11, 10), 'col2': np.random.randint(1, 11, 10),
#          'col3': np.random.randint(1, 11, 10)}
#
# df = pd.DataFrame(frame)


# 6
# Write a Pandas program to convert a given Series to an array.

# Solution
# frame = {'col1': np.random.randint(1, 11, 10), 'col2': np.random.randint(1, 11, 10),
#          'col3': np.random.randint(1, 11, 10)}
#
# df = pd.DataFrame(frame)
# print(type(df.to_numpy()))


# 7
# Write a Pandas program to convert a given Series to an array.

# Solution

# df = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
#
# def convert_to_series(series: np.ndarray):
#     new_arr = []
#
#     for values in series:
#         new_arr = [*new_arr, *values]
#
#     return pd.Series(new_arr)
#
#
# print(convert_to_series(df.to_numpy()))


# 8
# Write a Pandas program to convert a given Series to an array.

# Solution
# sorted_ser = pd.Series(np.arange(1, 20, 5)).sort_values()
#
# print(sorted_ser)


# 9
# Write a Pandas program to add some data to an existing Series.

# Solution
# ser = pd.Series(np.arange(1, 20, 5)).to_numpy()
#
# def append_series(array: np.ndarray, new_value: any):
#     return pd.Series([*array, new_value])
#
# print(append_series(ser, 1))


# 10
# Write a Pandas program to get the items of a given series not present in another given series.

# Solution

# may be solution is complicated, but I need to practice python skills too :)
# class ValuesNotExistInAnother:
#     def __init__(self, _first: np.ndarray, _second: np.ndarray):
#         self.first_arr = _first
#         self.second_arr = _second
#
#     @staticmethod
#     def binary_search(arr: np.ndarray, x: int):
#         low = 0
#         high = len(arr) - 1
#         mid = 0
#
#         while low <= high:
#             mid = (high + low) // 2
#             if arr[mid] < x:
#                 low = mid + 1
#             elif arr[mid] > x:
#                 high = mid - 1
#             else:
#                 return True
#
#         return False
#
#     def find_difference(self):
#         arr: np.ndarray = np.array([])
#
#         for number in self.first_arr:
#             if not self.binary_search(self.second_arr, number):
#                 arr = np.append(arr, number)
#
#         return pd.Series(arr)
#
#
# values = ValuesNotExistInAnother(pd.Series(np.arange(1, 6)).to_numpy(), pd.Series(np.arange(2, 11, 2)).to_numpy())


# 19 task web-site















