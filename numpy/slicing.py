import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]

# print(array[0:4:2]) ##  [[1 2 3 4], [9,10,11,12]] last index is exclusive
# print(array[::2])
# print(array[::-1])
# print(array[::-2])

# column selection
print(array[0,0]) # (row, column)
print(array[:, 0]) #1st column
print(array[:, -1]) #last column
print(array[:, 0:3]) 