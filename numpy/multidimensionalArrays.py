import numpy as np

# 2D Array
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,0,1,2]])

# 3D Array
threeDArray = np.array([[['A','B','C','D'], ['E','F','G','H'], ['I','J','K','L']],
                        [['M','N','O','P'], ['Q','R','S','T'], ['U','V','W','X']]])
##print(threeDArray.ndim)
##print(threeDArray.shape) ## (2,3,4) -> depth , rows , colums

print(threeDArray[0][0][0]) ##chain indexing works also on normal python
print(threeDArray[1,2,2]) ##Multidimensional Indexing only numpy
                          ##Multidimensional Indexing is faster than chain indexing

word = threeDArray[0,0,0] + threeDArray[0,2,2] + threeDArray[1,1,2] + threeDArray[0,1,3] + threeDArray[0,2,0] + threeDArray[1,1,3]
print(word)

