import numpy as np
import math
from typing import Union, List

# if you wanna practice with arrays and NumPy itself - welcome to:
# https://www.w3resource.com/python-exercises/numpy/index-array.php
# there are a lot of tasks. by the way, tasks and solutions below are from this webpage



# 1
# Task:
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Solution:
#arr = [12.23, 13.32, 100, 36.32]
#newArr = np.array(arr)



# 2
# Task:
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Solution:
# arr = np.arange(2, 11).reshape(3, 3)



# 3
# Task:
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# Solution:
# arr = np.zeros(10)
# arr[6] = 11



# 4
# Task:
# Write a NumPy program to create an array with values ranging from 12 to 38.

# Solution:
# arr = np.arange(12, 38)



# 5
# Task:
# Write a NumPy program to reverse an array (the first element becomes the last).

# Solution:
# arr = np.arange(12, 38)
# arr[::-1]



# 6
# Task:
# Write a NumPy program to convert an array to a floating type.

# Solution:
# arr = np.arange(1, 5)
# newFloatArray = np.asfarray(arr)
# print(newFloatArray)



# 7
# Task:
# Write a NumPy program to create a 2D array with 1 on the border and 0 inside.

# Solution:
# arr2d = np.ones((5, 5))
# arr2d[1:-1, 1:-1] = 0



# 8
# Task:
# Write a NumPy program to add a border (filled with 0's) around an existing array.

# Solution:

# my solution
# arr2d = np.zeros((5, 5))
# arr2d[1:-1, 1:-1] = 1

# web-site solution:
# newArr2d = np.pad(arr2d, pad_width=1, mode='constant', constant_values=0)
# print(newArr2d)



# 9
# Task:
# Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.

# Solution:
# checkerboard2dMatrix = np.zeros((8, 8))
#
# checkerboard2dMatrix[1::2, ::2] = 1
# checkerboard2dMatrix[::2, 1::2] = 1



# 10
# Task:
# Write a NumPy program to convert a list and tuple into arrays.

# Solution:
# def converter(values: Union[list, tuple]):
#     return np.asarray(values)
#
# print(converter([1, 2, 3, 4]))



# 11
# Task:
# Write a NumPy program to append values to the end of an array.

# Solution:

# my solution (think it is bad)

# array = np.arange(10, 40, 10)
# def appender(numpy_array: Union[List[int], np.ndarray], *values: int):
#     newArray = [*numpy_array, *values]
#     return np.array(newArray)
#
# print(appender(array, 1, 2, 3))

# best variant using built in functionality
# newArray = np.append(array, [[10, 30, 40]])



# 11
# Task:
# Write a NumPy program to append values to the end of an array.

# Solution:

# my solution (think it is bad)

# array = np.arange(10, 40, 10)
# def appender(numpy_array: Union[List[int], np.ndarray], *values: int):
#     newArray = [*numpy_array, *values]
#     return np.array(newArray)
#
# print(appender(array, 1, 2, 3))

# best variant using built in functionality
# newArray = np.append(array, [[10, 30, 40]])



# 12
# Task:
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy
# array

# Solution:
# centigrade = np.array([0, 12, 45.21, 34, 99.91])
# fahrenheit = (np.round((5 * centigrade / 9 - 5 * 32 / 9), 2))



# 13
# Task:
# Write a NumPy program to find the number of elements in an array. It also finds the length of one array element in
# bytes and the total bytes consumed by the elements.

# Solution:

# class LengthCounter:
#     def __init__(self, _array: np.ndarray):
#         self.array = _array
#
#     def get_total_length(self):
#         return len(self.array)
#
#     def get_length_of_one_in_bytes(self):
#         return self.array.itemsize
#
#     def get_length_of_all_in_bytes(self):
#         return self.array.nbytes
#
# arr = np.arange(1, 50)
# counter = LengthCounter(arr)



# 14
# Task:
# Write a NumPy program to find the number of elements in an array. It also finds the length of one array element in
# bytes and the total bytes consumed by the elements.

# Solution:
# firstArr = np.arange(0, 70, 10)
# secondArr = np.arange(0, 50, 40)
# print(np.in1d(firstArr, secondArr))



# 15
# Task:
# Write a NumPy program to find common values between two arrays.

# Solution:
# array_1 = np.array([0, 10, 20, 40, 60])
# array_2 = np.array([10, 30, 40])
# print(np.intersect1d(array_1, array_2))



# 16
# Task:
# Write a NumPy program to get the unique elements of an array.

# Solution:
# arr = np.array([10, 10, 20, 20, 30, 30])
# uniqueArr = np.unique(arr)



# 17
# Task:
# Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct
# values in array1 that are not in array2.

# Solution:
# arr1 = np.array([0, 10, 20, 40, 60, 80])
# arr2 = np.array([10, 30, 40, 50, 70, 90])
# difference = np.setdiff1d(arr1, arr2)
# print(difference)



# 18
# Task:
# Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return sorted, distinct values
# in only one (not both) of the input arrays.

# Solution:
# arr1 = np.array([0, 10, 20, 40, 60, 80])
# arr2 = np.array([10, 30, 40, 50, 70, 90])
# difference = np.setxor1d(arr1, arr2)



# 19
# Task:
# Write a NumPy program to construct an array by repeating.

# Solution:

# my solution
# def repeating_array(arr:np.ndarray, times: int):
#     new_arr = []
#
#     for i in range(times):
#         new_arr = [*new_arr, *arr]
#
#     return new_arr
#
# print(repeating_array(np.array([10, 30, 40, 50, 70]), 3))

# correct solution
# x = np.tile(np.array([10, 30, 40, 50, 70]), 3)



# 20
# Task:
# Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.

# Solution:
# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr.argmax())
# print(arr.argmin())