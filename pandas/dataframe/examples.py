import numpy as np
import pandas as pd


# create test and small dataframe

# np.random.seed(101)
# data = np.random.randint(0, 101, (4, 3))
# index = ['CA', 'NY', 'AZ', 'TX']
# columns = ['Jan', 'Feb', 'Mar']
#
# df = pd.DataFrame(data, index, columns)


# read csv file and create dataframe #
df = pd.read_csv('data.csv')


# use custom function for checking one value and based on the result add or change data in field #

# create custom function

# def salary_statistics(salary: int):
#     if salary < 3000:
#         return '$'
#     elif salary > 3000 & salary < 6000:
#         return '$$'
#     else:
#         return '$$$'
#
#
# use custom function

# df['salary_amount'] = df['salary'].apply(salary_statistics)


# use custom function for more than one values and add or change fields #

# create custom function we will work with

# def check_ratio(salary: int, price_per_hour: int):
#     # some stupid conditions
#     if salary > 3000 & price_per_hour < 30:
#         return 'ok'
#     elif salary > 5000 & price_per_hour > 50:
#         return 'ooooook'
#     else:
#         return 'not ok'

# two lines of code below are the same but speed of execution is not the same
# if we use "vectorize" answer we will get faster than using lambda function. this can show its face when we have
# big amounted of data. but documentation says that: "vectorize - was created for convenience, not for performance"

# df['salary_ratio'] = df.apply(lambda row: check_ratio(row['salary'], row['price_per_hour']), axis=1)
# df['salary_ratio'] = np.vectorize(check_ratio)(df['salary'], df['price_per_hour'])


# some other methods #

# df.describe() - descriptive statistics. this we can make "transpose()" - just for readability if you are need it
# df.sort_values("column name", ascending=True/False) - just sorting values. also you can use more than one column name
# df['column name'].max() - get max value
# df['column name'].idxmax() - get idx of max value
# df.iloc['index here'] - get value by idx
# df['column name'].value_counts() - count values
# df['column name'].unique() - get unique values
# df['column name'].nunique() - get number of unique values
# df['column name'].replace('field name from', 'and change to') - replace one or more than one values

# mymap = {'name from change': 'name to change', ...} - create map to replace values based on it
# df['column name'].map(mymap) - input prepared map above

# df.duplicated() - find duplicates
# df['column name'].between(10, 20, inclusive=True/False) - filter values between two values
# df.nlargest('value', 'column name') - return the first n rows with the largest values in columns,
# df.nsmallest('value', 'column name') - other way




