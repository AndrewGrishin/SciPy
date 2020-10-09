import pandas as pd
import numpy as np
from sklearn import linear_model

# Not universal option
# supports only linear regression
class fileParser:
    # replace all "," by "."
    def func(self,a):
        # creat a list from the string "a"
        x = list(a)
        for i in range(len(x)):
            # if I see a ",", I should change to "."
            if x[i] == ",":
                x[i] = "."
        # return rejoined string, but instead of "," there are only "."
        return "".join(x)

    # trains the model
    def regress(self, rnd = True):
        # creates a model with "self.df.shape[1] - 1" number of coeficents and one basis variable "f"
        # ASSUMPTION!!! it always will be the last column
        self.reg = linear_model.LinearRegression()
        # set free variables and a basis variable
        # and train this model, using data from the "my_csv.csv"
        self.reg.fit(self.df[list(self.df.columns)[0:-1:1]],self.df[list(self.df.columns)[-1]])

    # predicts the value of the function "f(x,y)"
    def predict(self, a):
        # if the shape of the "a" vector is not equal the nu,ber of variables
        # exception, with code 1
        if (len(a) != (self.df.shape[1] - 1)):
            print("Error")
            return 1
        print("f({:}, {:}) = {:.3f}".format(a[0],a[1],self.reg.predict([a])[0]))

    # read and parse file (write all strings to the array (numPy array), newType = float)
    def __init__(self,fileName):
        # creat a variable of a sample
        self.reg = []
        self.array = []
        self.df = []
        # try to open the file for parsing
        try:
            file = open(fileName,"r",encoding = "utf-8")
        except:
            # raise error if it was not successful
            raise "Error. There is no such file in your directory!"
        # skip the first line of the "file"
        next(file)
        #for each line in the file (parse the file and convert string numbers in float)
        for line in file:
            # split the line on three elements. Save them in the list "b"
            b = list(map(lambda a : a.split("\t"),list(line.split("\t"))))
            # convert each element to convertable view and convert them to "float"
            # after, save them to the list [a,b,c] and add append it to the "array"
            self.array.append([float(self.func(b[0][0])),float(self.func(b[1][0])),float(self.func(b[2][0]))])
        # close the file
        file.close()
        # define "self.df" by the newly parsed file
        self.df = pd.DataFrame(self.array)
        # name "self.df" columns
        self.df.columns = (["x" + str(i) for i in range(self.df.shape[1] - 1)] + ["f"])

# creates a smaple of the class
sample = fileParser(input("Input the name of the file: "))
# start regression and training porcess
sample.regress()
# delete the object, cause we will never need it anymore
del(sample)

# z = z(x,y)
# z = a*x + b*y + c
# z = y ^ 2 + x !!!