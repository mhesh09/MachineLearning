# importing libraries
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler

# data set link
url = "file:///home/cooldevil/Documents/MachineLearning/Program/data-01"
# data parameters
names = ['Date', 'Time', 'Code', 'Vallue']

# preparating of dataframe using the data at given link and defined columns list
dataframe = pandas.read_table(url, names = names)
array = dataframe.values


# separate array into input and output components
X = array[:,0:4]

Y = array[:,3]


# initialising the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))


# learning the statistical parameters for each of the data and transforming
rescaledX = scaler.fit_transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
