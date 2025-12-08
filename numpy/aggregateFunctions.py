import numpy as np

## Summarize data and return typically a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array)) ## standard deviation
# print(np.var(array)) ## variance
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array)) ## index of min value
# print(np.argmax(array))

print(np.sum(array, axis = 0)) ## axis = 0 means all colums
print(np.sum(array, axis = 1)) ## axis = 1 means all rows

