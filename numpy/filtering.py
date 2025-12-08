import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

## This is Boolean Indexing. doing these following gives output as a flat array.
# So dimension is not preserved
# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages >= 65]

# print(teenagers, adults, seniors)

## To preserve teh dimension we use where function

adults = np.where(ages >= 18, ages, 0) ## (condition, array, fill value for ones those do not satisfy condition)
# print(adults)

