import numpy as np
from scipy import integrate

def func(x):
    return 1 / (x**2) + x**3

"""def integrate(f,a,b,n):
    k = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + k / a + i * k)
    return s * k

n = 1
#while (not abs(abs(integrate(function,1,5,n * 2)) - abs(integrate(function,1,5,n))) < 1E-4):
#    n += 1
#print(n)"""

def monteCarloIntegration(func, a = 0, b = 1, n = 1000000000):
    subsets = np.arange(0, n + 1, n / 10)
    u = np.zeros(n)
    for i in range(10):
        s = int(subsets[i])
        e = int(subsets[i + 1])
        u[s:e] = np.random.uniform(low = i / 10, high = (i + 1) / 10, size = e - s)
    np.random.shuffle(u)
    return (b - a) / n * (func(a + (b - a) * u).sum())

#print(integrate(function,1,10,10000000))

print(abs(abs(integrate.quad(func, 1, 4)[0]) - abs(monteCarloIntegration(func, 1, 4))))