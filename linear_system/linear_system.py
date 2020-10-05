from scipy import linalg
import numpy as np
from random import randint
import sys

usedColumns = []

matrix = np.array(
    [[2.0,1.0,2.0],
    [1.0,2.0,1.0],
    [3.0,1.0,-1.0]]
)

b = np.array([10.0,8.0,2.0])

for vector,indVec in zip(matrix,range(len(matrix))):
    for value, indVal in zip(vector,range(len(vector))):
        if (value != 0 and indVal not in usedColumns):
            usedColumns.append(indVal)
            vector /= value
            b[indVec] /= value
            break
    for ind in range(len(matrix)):
        if (ind == indVec): continue
        if (sum(1 for val in vector if val == 0) == len(vector) and b[indVec]):
            print("This system is inconsistent!")
            sys.exit(1)
        if (matrix[ind][usedColumns[-1]] != 0):
            b[ind] -= b[indVec] * matrix[ind][usedColumns[-1]] #vec[usedColumns[-1]]
            matrix[ind] -= matrix[indVec] * matrix[ind][usedColumns[-1]] #vec[usedColumns[-1]]


print(matrix)
print(b)