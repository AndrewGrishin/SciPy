from scipy import linalg
import numpy as np
from random import randint

n = randint(1,7)
#A = np.array([[randint(-8,9) for i in range(n)] for j in range(n)])
#b = np.array([randint(-50,51) for i in range(n)])

A = np.array([[1,2],[2,4]])
b = np.array([3,6])
x = linalg.solve(A,b)

print(x)