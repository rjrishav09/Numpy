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