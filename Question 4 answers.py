import numpy as np
array1 = np.random.randint(1, 101, size=(4, 4))

row_array = array1.reshape(2, 8)
column_array = array1.T.reshape(2, 8)

sum_row_column = lambda array: np.array([np.sum(array, axis=1), np.sum(array, axis=0)])

sums_row = sum_row_column(row_array)
sums_column = sum_row_column(column_array)

print("Original Array:")
print(array1)
print("\nRow Array:")
print(row_array)
print("\nColumn Array:")
print(column_array)
print("\nSum of each row:")
print(sums_row)
print("\nSum of each column:")
print(sums_column)
