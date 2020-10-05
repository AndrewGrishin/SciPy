from scipy import linalg
import numpy as np
from random import randint
import sys

def solveMatrixUsingGaussJordanMethod(matrix, b, rnd = None):
    matrixLocal = np.copy(matrix)

    matrixEquationTask = open("matrixEquationTask.txt","w")
    matrixEquationTask.write("Initial matrix. Shape -> (" + str(len(matrixLocal)) + ", " + str(len(matrixLocal[0])) + ")\n\t")
    for vector,index in zip(matrixLocal,range(len(matrixLocal))):
        matrixEquationTask.write(" ".join(map(lambda f : str(format(f,"." + str(rnd) + "f") if rnd else f),vector)) + " = " + str(format(b[index],"." + str(rnd) + "f") if rnd else b[index]) + "\n\t")
    matrixEquationTask.write("\n")

    usedColumns = []
    for vector,indVec in zip(matrixLocal,range(len(matrixLocal))):
        for value, indVal in zip(vector,range(len(vector))):
            if (value != 0 and indVal not in usedColumns):
                usedColumns.append(indVal)
                vector /= value
                b[indVec] /= value
                break
        for ind in range(len(matrixLocal)):
            if (sum(1 for val in vector if val == 0) == len(vector) and b[indVec]):
                matrixEquationTask.write("This system is inconsistent!\n")
                sys.exit(1)
            if (ind == indVec): continue
            if (matrixLocal[ind][usedColumns[-1]] != 0):
                b[ind] -= b[indVec] * matrixLocal[ind][usedColumns[-1]]
                matrixLocal[ind] -= matrixLocal[indVec] * matrixLocal[ind][usedColumns[-1]]

    matrixEquationTask.write("Final matrix.\n\t")
    for vector,index in zip(matrixLocal,range(len(matrixLocal))):
        matrixEquationTask.write(" ".join(map(lambda f : str(format(f,"." + str(rnd) + "f") if rnd else f),vector)) + " = " + str(format(b[index],"." + str(rnd) + "f") if rnd else b[index]) + "\n\t")
    matrixEquationTask.close()

    del(usedColumns)
    del(matrixLocal)


matrix = np.array(
    [[2.0,1.0,7.0,5.0],
    [1.0,2.0,1.0,3.0],]
)
b = np.array([1.0,-1.0])

solveMatrixUsingGaussJordanMethod(matrix,b,3)