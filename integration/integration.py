import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
import time

def func(x):
    return math.sin(x) * math.cos(math.sin(x))

def monteCarloIntegration(func, a = 0, b = 1, n = int(1E7)):
    start = time.time()
    xvalues = a + (b - a) * np.random.uniform(low = 0, high = 1, size = n)
    #fvalues = map(func,xvalues)
    return (sum(map(func,xvalues)) * (b - a) / n, time.time() - start)

def mci(func, a = 1, b = 1, n = int(1E7)):
    start1 = time.time()
    subsets = np.arange(0, n + 1, n / 10)
    u = np.zeros(n)
    for i in range(10):
        start, end = int(subsets[i]), int(subsets[i + 1])
        u[start:end] = np.random.uniform(low = i / 10, high = (i + 1) / 10, size = end - start)
    np.random.shuffle(u)
    return (sum(map(lambda f : func(a + (b - a) * f) ,u)) * (b - a) / n, time.time() - start1)

c = integrate.quad(func, 0, math.pi)
print("SciPy ->", c[0], "\n")
a = monteCarloIntegration(func, 0, math.pi)
print("Monte Carlo One ->\t", a[0], "\n\tExecution time ->", a[1], "\n\tDifference (abs) ->", (100 * abs(c[0] - a[0]) / c[0]), "%\n")
b = mci(func, 0, math.pi)
print("Monte Carlo Two ->\t", b[0], "\n\tExecution time ->", b[1], "\n\tDifference (abs) ->", (100 * abs(c[0] - b[0]) / c[0]), "%")