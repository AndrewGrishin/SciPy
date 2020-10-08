import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
import time

def func(x):
    return math.sin(x)

def monteCarloIntegration(func, a = 0, b = 1, n = 10):
    xvalues = a + (b - a) * np.random.uniform(low = 0, high = 1, size = n)
    xvalues += (a + (b - a) * np.random.uniform(low = 0, high = 1, size = n))
    plt.plot(xvalues)
    fvalues = np.array(list(map(func,xvalues)))
    plt.show()
    print(sum(fvalues * (b - a) / n))

    


print("SciPy -> ",integrate.quad(func, 0, math.pi)[0])
print(monteCarloIntegration(func, 0, math.pi,1000000))