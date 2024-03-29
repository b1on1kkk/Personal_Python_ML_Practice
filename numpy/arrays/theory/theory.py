# just let you know: I think this is not a "theory", this is a short commands what you need to understand NumPy.
# also, its enough knowledge to start solving NumPy problems :)


# BUILD-IN ARRAY FUNCTIONALITY

# print(np.arange(0, 5)) - numpy array with 5 elements
# print(np.arange(0, 101, 2)) - numpy array with step of 2
# print(np.zeros((5, 5))) - numpy array of zero matrix
# print(np.ones((5, 5))) - same as zero matrix but this matrix consists of ones
# print(np.linspace(0, 10, 3))  - numpy array with equidistant values (in this way will have 3 values)
# print(np.eye(5)) - identity matrix


# print(np.random.rand(5, 5)) - get matrix 5X5 with random values between 0 and 1
# print (np.random.randn(5, 5)) - return a sample (or samples) from the "standard normal" distribution.
# print(np.random.randint(0, 100, (5, 5))) - return random values from 0 to 100 in 5X5 matrix


# arr = np.arange(0, 25)
# arr.reshape(5, 5) # - reshape to 5X5 matrix

# arr = np.random.randint(0, 100, 10)
# print(arr.max()) # - get max NUMBER in array
# print(arr.argmax()) # - get INDEX of max number in array

# arr.dtype - just attribute to understand which datatype is in array
# arr.shape - get number of dimensions


# asfarray - convert integer numpy array into floating array

# example:
# arr = np.arange(1, 5)
# newFloatArray = np.asfarray(arr)







# ARITHMETICAL METHODS ON ARRAYS #

#array_1 = np.arange(0, 5)

# print(array_1 + 5) - +5 to every element in array
# print(array_1 - 5) - -5 to every element in array

#array_2 = np.arange(0, 5)

# print(array_1 + array_2) - return sum of array. notice that array length must be equal

# and other methods like: *, /, sqrt, sin, log...

# print(array_1.sum()) - return sum of all values in array
# print(array_1.mean()) - return averange value of array

# array2d = np.arange(0, 25).reshape(5, 5) # - generate array 5X5 2d matrix

# print(array2d.sum(axis=0)) # - sum of columns
# print(array2d.sum(axis=1)) # - sum of rows