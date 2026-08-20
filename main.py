# N-Dimensional array:
import numpy as np
array = np.array([1,2,3])
array = array*2
print(array)

# Multi-Dimensional array:
array1 = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                    [["J","K","L"],["M","N","O"],["P","Q","R"]],
                    [["S","T","U"],["V","W","X"],["Y","Z","ZA"]]])
# Chain Indexing
print(array1[0][0][0])

# Multi-Dimensional Indexing

print(array1[0,0,0])

# Word Formation using Catenation:
word = array1[0,0,0] + array1[1,2,2] + array1[2,2,1] + array1[2,0,2] + array1[1,1,1]
print(f"Your name is: {word}")

# Check the number of dimension:
print(array.ndim)
print(array1.ndim)

# Check the shape of array: