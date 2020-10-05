from scipy import linalg
import numpy as np
from random import randint

used = []
strings = 3
columns = 3

matrix = np.array(
    [[5.0,0.0,3.0],
    [1.0,4.0,7.0],
    [0.0,0.0,2.0]]
)

b = np.array([3.0,1.0,8.0])

for vector,indVec in zip(matrix,range(len(matrix))):
    print(matrix)
    print(b)
    print()
    for value, indVal in zip(vector,range(len(vector))):
        if (value != 0 and indVal not in used):
            used.append(indVal)
            matrix[indVec] /= value
            b[indVec] /= value
            break
    
print(matrix)
print(b)

"""
a b c | d1 (/a) (a != 0)
e f g | d2
h i j | d3

1 b/a c/a | d1/a (*e)
e   f   g | d2
h   i   j | d3

e e*b/a e*c/a | e*d1/a 
e     f     g | d2
h     i     j | d3

"""