import numpy as np
import tsp

# read and parse file (write all strings to the array (numPy array), newType = float)
def txtToData(fileName):
    # creat a variable of sample
    array = []
    # try to open the file for parsing
    try:
        file = open(fileName,"r",encoding = "utf-8")
    except:
        # raise error if it was not successful
        raise "Error. There is no such file in your directory!"
    #for each line in the file (parse the file and convert string numbers in float)
    for line in file:
        # after, save them to the list [a,b,c] and add appendit to the "array"
        array.append(np.array(list(map(lambda a : float(a) if (a != "_") else np.inf,line.replace("\n","").replace("_",str(np.inf)).split(" ")))))
    # close the file
    file.close()
    # return the array of NumPy arrays (convetred string of the file)
    return np.array(array)

# creates a file to write results
travelling_salesman = open("travelling_salesman.txt","w")
# parse the file and gather the information (initial matrix)
salesManMatrix = txtToData(input("Input the name of the file: "))
# create a dictionary {node: cost}
dictionary = {(i,j) : salesManMatrix[i][j] for i in range(len(salesManMatrix)) for j in range(len(salesManMatrix))}
# use the module "tsp" to solve the "Travelling Salesman Problem"
path = tsp.tsp(range(len(salesManMatrix)), dictionary)
# write the initial commutating matrix into the file "travelling_salesman.txt"
travelling_salesman.write("Initial Commutating Matrix: \n\t")
travelling_salesman.write("\n\t".join(map(str,salesManMatrix)).replace("[","").replace("]","") + "\n\n")
# write the value of the shortest path
travelling_salesman.write("The shortest path costs -> " + str(path[0]) + "\n\n")
travelling_salesman.write("Nodes were used:\n\t")
# pretty print (nothing interesting)
for i in range(len(path[1])):
    address = (path[1][i],path[1][i+1] if (i + 1) < len(path[1]) else path[1][0])
    travelling_salesman.write(str(address) + " -> " + str(dictionary[address]) + "\n\t")
# close the file "travelling_salesman.txt"
travelling_salesman.close()