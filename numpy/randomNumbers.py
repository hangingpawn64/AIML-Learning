import numpy as np

rng = np.random.default_rng(seed = 1)

print(rng.integers(low = 1,high = 101, size = (3, 2)))

# np.random.seed(seed=1)
print(np.random.uniform(low = -1, high = 1, size = (2,3))) ## floating point numbers

## Shuffling an array

array = np.array([1, 2, 3, 4, 5])

rng1 = np.random.default_rng()

rng.shuffle(array)
print(array)

fruits = np.array(["apple", "banana", "orange", "coconut", "pineapple"])
fruit = rng1.choice(fruits)
print(fruit)

randomFruits = rng.choice(fruits, size = (3,3))
print(randomFruits)


## Exercise : 2D array of randomly selected emojis

emojis = np.array([["😃", "😄", "🤣"],
                    ["🥲", "🥰", "😘"],
                    ["😇", "😎", "😡"]])
randEmoji = rng1.choice(emojis , size = (2,3))
print(randEmoji)
