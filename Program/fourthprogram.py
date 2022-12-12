import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import preprocessing


data_set = pd.read_csv("file:///home/cooldevil/Documents/MachineLearning/Program/Data_for_Feature_Scaling.csv")
data_set.head()

x= data_set.iloc[:,1:3].values

print("\nOriginal Data Value", x)

min_max_scalar = preprocessing.MinMaxScaler(feature_range=(0,1))

x_after_min_max_sclar = min_max_scalar.fit_transform(x)

print("\n Afer min_max scaling: \n",x_after_min_max_sclar)

Standardisation = preprocessing.StandardScaler()

x_after_Standardisation = Standardisation.fit_transform(x)

print("\n X after Standardization", x_after_Standardisation)


