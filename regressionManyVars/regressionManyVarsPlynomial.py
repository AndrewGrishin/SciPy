import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# NonLinear MultiVariable Regression
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

    # read and parse file (write all strings to the array (numPy array), newType = float)
    def __init__(self,fileName):
        # creat variables of a sample
        self.pipe = ""
        self.df = ""
        # try to open the file for parsing
        try:
            file = open(fileName,"r",encoding = "utf-8")
        except:
            # raise error if it was not successful
            raise "Error. There is no such file in your directory!"
        # skip the first line of the "file"
        next(file)
        # create a local variable for parser converting
        array = []
        #for each line in the file (parse the file and convert string numbers in float)
        for line in file:
            # split the line on three elements. Save them in the list "b"
            b = list(map(lambda a : a.split("\t"),list(line.split("\t"))))
            # convert each element to convertable view and convert them to "float"
            # after, save them to the list [a,b,c] and add append it to the "array"
            array.append([float(self.func(b[0][0])),float(self.func(b[1][0])),float(self.func(b[2][0]))])
        # close the file
        file.close()
        # set array as a pd.DataFrame
        self.df = pd.DataFrame(array)
        # name "self.df" columns
        self.df.columns = (["x" + str(i) for i in range(self.df.shape[1] - 1)] + ["f"])

    # trains the model
    def regress(self, rnd = True):
        # polynomial regression is 2 steps process
        # first -> transform data into polynomial ("PolynomicalFeaturs()")
        # second -> use Linear Regression
        # to automate this process -> use Pipelines
        # here creates steps of NonLinear Regression
        input = [("polynomial",PolynomialFeatures(degree = 2)), ("modal",LinearRegression())]
        # creates model "pipe", using these steps
        self.pipe = Pipeline(input)
        # creates a model with "self.df.shape[1] - 1" number of coeficents and one basis variable "f"
        # ASSUMPTION!!! it always will be the last column
        # train the model
        self.pipe.fit(self.df[list(self.df.columns)[0:-1:1]],self.df[list(self.df.columns)[-1]])
    
    # predicts the value of the function "f(x,y)", using trained model "self.pipe"
    def predict(self, a):
        # if ther len of "a" vector is not equal to the number of columns in the initial file
        if (len(a) != (self.df.shape[1] - 1)):
            # print error
            print("Error")
            # shut the programme down
            sys.exit(1)
        # else -> return the predicted value of the function
        return self.pipe.predict([a])[0]

# plot the picture in 3d from the matrics "array"
def pictureFromArray(df, how = "plot"):
    # convert to numPy array
    na = np.array(df)
    # creating a figure with matplotlib (form)
    figure = plt.figure()
    # adding 3'rd dimention
    ax = figure.add_subplot(111,projection = "3d")
    # add to figure data needed for Visualisation (here is split my matrix on three arrays by colomns)
    # also this method gets parameter "how", which should be a string
    # decribing, how should the graph be visualised "plot" of "scatter"
    ax.plot(na[:,0],na[:,1],na[:,2]) if how == "plot" else ax.scatter(na[:,0],na[:,1],na[:,2])
    # change the lable of X-axes
    ax.set_xlabel("X-axes")
    # change the lable of Y-axes
    ax.set_ylabel("Y-axes")
    # change the lable of Z-axes
    ax.set_zlabel("Z-axes")
    # save the picture (now commented)
    #plt.savefig("MatPlotLib_picture_plot.png") if how == "plot" else plt.savefig("MatPlotLib_picture_scatter.png")
    # show the final graph
    plt.show()

# creates a sample of the fileParse to get the information from the file
sample = fileParser(input("Input the name of the file: "))
# start the NonLinear Polynomial regression
sample.regress()
# create a longer list of variables, used in the file "my_csv.csv"
fvalues = [[a[0],a[1],sample.predict(a)] for a in zip(list(sample.df["x0"]) + [float(i) + 0.1 for i in range(10,110)], list(sample.df["x1"]) + [i for i in range(0,-100,-1)])]
# plot the graph of the model, after regression process and training
pictureFromArray(pd.DataFrame(fvalues))
# plot the inital data, stored in the file "my_csv.csv"
pictureFromArray(sample.df)
# delete the object, cause we will never need it anymore
del(sample)

# z = z(x,y) -> assumption
# z = a*x + b*y + c -> impossible suggestion
# z = y ^ 2 + x -> possible assumption (but not the single)
# statistics -> result (coeficients), R^2, fStatistics !!!
