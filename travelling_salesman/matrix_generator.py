import numpy as np

file = open("matrix.txt","w")

for line in range(200):
    na = list(map(str,np.random.randint(low = 2, high = 33, size = 200)))
    na[line] = "_"
    file.write(" ".join(map(str,na)) + "\n")

file.close()
