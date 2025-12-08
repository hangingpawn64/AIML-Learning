import numpy as np

# Scalar Arithmetic

# array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

## Vectorized math funcs

array = np.array([1.01, 2.5, 3.99])

# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))
# print(np.pi)

# EXERCISE

radii = np.array([1, 2, 3])

# print(np.pi * radii ** 2)

## Element-wise Arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

## Comparision Operators

scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores == 100) # False False True False False False
# print(scores >= 60)  # True False True True True True

scores[scores < 75] = 0
scores[scores >= 75] = 1

# print(scores)