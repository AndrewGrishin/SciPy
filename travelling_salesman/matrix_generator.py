import numpy as np

file = open("matrix.txt","w")

for line in range(20):
    na = list(map(str,np.random.randint(low = 2, high = 33, size = 20)))
    na[line] = "_"
    file.write(" ".join(map(str,na)) + "\n")

file.close()
