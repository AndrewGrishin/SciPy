from scipy import linalg
import numpy as np
from random import randint
import sys

# "eigenTask" function gets 2 parameters (the matrix to twork with, the number of the digit, by what all calculations should be rounded)
# "eigenTask" function returns nothing
# "eigenTask" function computes:
#   -> eigen values of the matrix
#   -> eigen vectors of the matrix
# "eigenTask" function writes all the gained information into the file "eigenTask.txt"
# if this file already exists, it REWRITES it
def eigenTask(matrix, rnd = None):
    # create file "eigenTask.txt" to "write" data into it
    eigenTask = open("eigenTask.txt","w")
    # write into the file "eigenTask.txt" what the shape of inputed matrix is
    eigenTask.write("Initial matrix's shape -> (" + str(len(matrix)) + ", " + str(len(matrix[0])) + ")\n")
    # write into the file "eigenTask.txt" the whole inputed matrix
    eigenTask.write(str(matrix) + "\n\n")
    # get "eigen the values" and "eigen vectors" of the "matrix" using scipy.linalg.eig(:_)
    eigenValues, eigenVectors = linalg.eig(matrix)
    # write into the file "eigenTask.txt" how many "eigen values" this "matrix" has
    eigenTask.write("This matrix has " + str(len(eigenValues)) + " eigen values.\n")
    # start the cycle through the array of "eigen values", using zip(:_,:_) to have indeces of "eigen values"
    for (value, index) in zip(eigenValues,range(len(eigenValues))):
        # write into the file "eigenTask.txt" "matrix's" "eigen values", one on each line
        # use round, if parameter "rnd" is set on some not "None" value
        eigenTask.write("\t" + str(index + 1) + ") " + "".join(list(str(format(value,"." + str(rnd) + "f")) if rnd != None else list(str(value)))) + "\n")
    # write into the file "eigenTask.txt" how many "eigen vectors" this "matrix" has
    eigenTask.write("\nThis matrix has " + str(len(eigenVectors)) + " eigen vectors.\n")
    # start the cycle through the array of "eigen vectors", using zip(:_,:_) to have indeces of "eigen vectors"
    for vector, index in zip(eigenVectors, range(len(eigenVectors))):
        # write "eigen vectors" of the "matrix" into the file "eigenTask.txt", one on each line
        # use round, if parameter "rnd" is set on some not "None" value
        eigenTask.write("\t x_" + str(index) + "\n\t\t" + "\n\t\t".join(list(map(lambda a : str(format(a,"." + str(rnd) + "f") if rnd != None else str(a)),vector))) + "\n")
    # close the file "eigenTask.txt"
    eigenTask.close()

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
matrix = np.array([list(map(float,line.split(" "))) for line in file])

# if the shape of the matrix is NOT squared => raise error
if (len(matrix[0]) != len(matrix)):
    error = open("MatrixShapeError.txt","w")
    # write information about the error into the file "errors.txt"
    error.write("MatrixShapeError: Shape of the matrix must have equal number of rows and columns! Please, try again.\n\n")
    # write information to attract attention into the standart output stream (terminal)
    print("Check the file \"MatrixShapeError.txt\" a new error has just occured.")
    # close "MatrixShapeError.txt" file
    error.close()
    # give the control back to the Operation System (stop the programme)
    sys.exit(2)

# call the function "eigenTask" with numbers, rounded to the 3'rd digit
eigenTask(matrix,rnd = 3)
# print into the standart output stream (terminal), that the programme has succeeded
print("Process\t" + "-" * 13 + "> OK")
print("Result\t" + "-" * 13 + "> \"eigenTask.txt\"")