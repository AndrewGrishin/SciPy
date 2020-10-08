import numpy as np
from scipy import integrate
import math
import time

# initial function to integrate
def func(x):
    # func(x) = sin(x) * cos(sin(x))
    return math.sin(x) * math.cos(math.sin(x))

# the first release of integration algorithm (n = number of dots)
def monteCarloIntegration(func, a = 0, b = 1, n = int(1E7)):
    # start is required to check the time, what it takes the function to execute
    # start it the "starting point"
    start = time.time()
    # Monte Carlo uses very interesint method to count integrals
    # it DOES NOT sum the areas successively, it "throw" n dots on the [a;b]
    # for each n(i), we find func(n(i))
    # for each func(n(i)) find the area
    # sum all func(n(i))
    # multiply the "sum" by the size of each interval (b - a) / n
    # where "n" = number of intervals
    # in other words, "xvalues" is a NumPy array, each element of which defines as: a + (b - a) * t, where "t" lies in [0;1]
    xvalues = np.zeros(n)
    xvalues = a + (b - a) * np.random.uniform(low = 0, high = 1, size = n)
    # this thought is in between, just not to forget,
    # that what "map(func,xvalues)" is
    # fvalues = map(func,xvalues)
    # time.time() - start = time between the beginging of the execution of the function and the end of it
    return (sum(map(func,xvalues)) * (b - a) / n, time.time() - start)

# the second release of integration algorithm (n = number of dots)
def mci(func, a = 1, b = 1, n = int(1E7)):
    # start1 is required to check the time, what it takes the function to execute
    # start1 it the "starting point"
    start1 = time.time()
    # create a new sub-NumPy.array define the whole "u" array, only in 10 cycles
    # "n" is 1E7 by default, "n" / 10 = 1E6, the step is SO BIG,
    # but there are only 10 elements in the "subsets" [0., 1E6, 2 * 1E6, ..., 10 * 1E6]
    subsets = np.arange(0, n + 1, n / 10)
    # create the NumPy array to "throw" dots on the [a;b]
    u = np.zeros(n)
    # here we start our loop, that does not depend on the length of "u"
    for i in range(10):
        # define "start" as the first (starting index)
        # define "end" as the second (lasting index)
        start, end = int(subsets[i]), int(subsets[i + 1])
        # all elements in range [start,end] are now defined as random elements from the range of [i / 10; (i + 1) / 10]
        # this feature gives additional accuracy looking for the element in between of [i / 10; (i + 1) / 10]
        # BUT it (this feature) makes the algorithm almost "two times longer"
        u[start:end] = np.random.uniform(low = i / 10, high = (i + 1) / 10, size = end - start)
    # shuffle the "u" array
    np.random.shuffle(u)
    # count the sum (same idea) as in "the first release"
    return (sum(map(lambda f : func(a + (b - a) * f), u)) * (b - a) / n, time.time() - start1)

# create a file "integrationTask.txt" to write results in
integrationTask = open("integrationTask.txt","w")
# use SciPy library (module "integrate", function ".quad") to compare results
c = integrate.quad(func, 0, math.pi)
integrationTask.write("SciPy -> " + str(c[0]) + "\n\n")
a = monteCarloIntegration(func, 0, math.pi)
# prints to the standart output stream the (values, time, absolute difference comparing to the "a" in %)
integrationTask.write("Monte Carlo One ->\t" + str(a[0]) + "\n\tExecution time -> " + str(a[1]) + "\n\tDifference (abs) -> " + str(100 * abs(c[0] - a[0]) / c[0]) + " %\n\n")
b = mci(func, 0, math.pi)
# prints to the standart output stream the (values, time, absolute difference comparing to the "a" in %)
integrationTask.write("Monte Carlo One ->\t" + str(b[0]) + "\n\tExecution time -> " + str(b[1]) + "\n\tDifference (abs) -> " + str(100 * abs(c[0] - b[0]) / c[0]) + " %\n")
# close the file "integrationTask.txt", as all result are already there
integrationTask.close()