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

# start "try" -> "except" block, to check if the inputed file extsts
try:
    # try to open the file, the name of which was entered
    file = open(input("Input the file name, where the matrix is: "),"r")
except FileNotFoundError:
    # Create a new file "errors.txt", to write all errors in
    error = open("FileNotFoundError.txt","w")
    # if error "FileNotFound" occures => there is no such file in this directory
    # write into the file "errors.txt" that there is no such file in the current directory
    error.write("FileNotFound: There is no such file in current directory! Please, try again.\n\n")
    # write into the standart output (terminal), that a new file has been created
    print("Check the file \"FileNotFoundError.txt\" a new error has just occured.")
    # close "FileNotFoundError.txt" file
    error.close()
    # give the control back from the current programme to the Operation System
    sys.exit(1)

# if everything is "ok" => split the matrix from the file into the normal matrix
# "matrix" is only n-1 rows and the last one is "b" vector
# "*matrix" and "b" -> are <class, list> => need to convert them to NumPy arrays
*matrix,b = np.array(np.array([list(map(float,line.split(" "))) for line in file]))
# close the file with the input information
file.close()

# call the function "solveMatrixUsingGaussJordanMethod" with numbers, rounded to the 3'rd digit
solveMatrixUsingGaussJordanMethod(np.array(matrix),np.array(b),rnd = 3)
# print into the standart output stream (terminal), that the programme has succeeded
print("Process\t" + "-" * 13 + "> OK")
print("Result\t" + "-" * 13 + "> \"matrixEquationTask.txt\"")