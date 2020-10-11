import numpy as np
import sys

# Ax=b
# the function gets the matrix of coefficients (A matrix), the "b vector" and "rnd" parameter, telling up to what digit should the results be rounded
def solveMatrixUsingGaussJordanMethod(matrix, b, rnd = None):
    # create copy of the matrix, given to the function
    # link transfer => if we change the "matrix" in this function => we change it in the memory
    # because we are working with its address in RAM
    matrixLocal = np.copy(matrix)
    # creates a file to write results in
    matrixEquationTask = open("matrixEquationTask.txt","w")
    # writes into the file "matrixEquationTask.txt" information about INITIAL "matrixLocal" (copy of the "matrix")
    matrixEquationTask.write("Initial matrix. Shape -> (" + str(len(matrixLocal)) + ", " + str(len(matrixLocal[0])) + ")\n\t")
    # start a loop to write each vector appropriately (here also are some appearance changes) into the file "matrixEquationTask.txt"
    # Nothing interesting and essentially necessary
    for vector,index in zip(matrixLocal,range(len(matrixLocal))):
        matrixEquationTask.write(" ".join(map(lambda f : str(format(f,"." + str(rnd) + "f") if rnd else f),vector)) + " = " + str(format(b[index],"." + str(rnd) + "f") if rnd else b[index]) + "\n\t")
    matrixEquationTask.write("\n")
    # create a list to write the "index" of the element in the "vector", which was "chosen as leading"
    # the idea is no to make 1-s of elements in the same column
    # it does not result in something useful
    usedColumns = []
    # start the loop through "vector" and "index" of the vector in "matrixLocal"
    for vector,indVec in zip(matrixLocal,range(len(matrixLocal))):
        # choose a non-zero "value" element in each "vector" to be "leading"
        for value, indVal in zip(vector,range(len(vector))):
            # check if the element is (NOT equal to 0 && is NOT in "usedColumns")
            # condition (NOT in "usedColumns") tells, that this column has not been chosen before
            if (value != 0 and indVal not in usedColumns):
                # if we have found it, we add it into the "usedColumns", because we will never use it again
                usedColumns.append(indVal)
                # we divide each element in the current "vector" by this "value"
                # type of the "vector" is NumPy.array(), so it applies devision to each element in it
                vector /= value
                # we also divide the "b vector" value of current "vector"
                b[indVec] /= value
                # after it we break this loop
                break
        # start the loop to substract the leading "vector" with the leading "value" from other "vectors"
        for ind in range(len(matrixLocal)):
            # check if the "ind" "vector" is zero-vector and its "b vector" value is not zero
            # here "sum()" function is applied to count zeroes in the "ind" vector
            if (sum(1 for val in vector if val == 0) == len(vector) and b[indVec]):
                # if it is true => the programme write that this system is inconsistent to the "matrixEquationTask.txt" file
                matrixEquationTask.write("This system is inconsistent!\n")
                # the execution of the programme stops
                # the control goes back to the Operation System by the exception with the code "1"
                sys.exit(1)
            # if the "current vector" is the leading one => skip this part of the loop
            if (ind == indVec): continue
            # if the value at the "ind" row and the "leading column" is not zero
            if (matrixLocal[ind][usedColumns[-1]] != 0):
                # then substract "b vector" value of the indVec (leading row)
                # muliplied by the "ind" value in the last used "leading column" 
                # from the "ind" "b vector" value
                # b(ind) - b(indVec) * matrix(ind, usedColumns(-1))
                b[ind] -= b[indVec] * matrixLocal[ind][usedColumns[-1]]
                # same thing with the "ind" vector and the "indVec" (leading vector) "vector"
                # substract leading vector, multiplied by "ind" values in the leeding "column" from the "ind" vector
                # matrix(ind) - matrix(indVec) * matrix(ind,usedColumns(-1))
                matrixLocal[ind] -= matrixLocal[indVec] * matrixLocal[ind][usedColumns[-1]]
    # writes into the file "matrixEquationTask.txt" the the INITIAL "matrixLocal" (copy of the "matrix") after the changes
    # start a loop to write each vector appropriately (here also are some appearance changes)
    # Nothing interesting and essentially necessary
    matrixEquationTask.write("Final matrix.\n\t")
    for vector,index in zip(matrixLocal,range(len(matrixLocal))):
        matrixEquationTask.write(" ".join(map(lambda f : str(format(f,"." + str(rnd) + "f") if rnd else f),vector)) + " = " + str(format(b[index],"." + str(rnd) + "f") if rnd else b[index]) + "\n\t")
    matrixEquationTask.close()
    # delete local vars as "usedColumns" and "matrixLocal" (copy of the "matrix"), as we do not need them anymore
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

# check in SciPy!!!!
