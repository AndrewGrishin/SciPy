import numpy as np

file = open("matrix.txt","w")

for line in range(4):
    na = list(map(str,np.random.randint(low = 1, high = 1000, size = 4)))
    na[line] = "_"
    file.write(" ".join(map(str,na)) + "\n")

file.close()
