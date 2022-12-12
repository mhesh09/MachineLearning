import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

data = pd.read_csv("creditcard.csv")

# print(data.info())

data['normAmount']= StandardScaler().fit_transform(np.array(data['Amount']).reshape(-1,1))

data = data.drop(['Time','Amount'], axis = 1)
print(data['Class'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(data, test_size=0.3, random_state=0)

print("Number transactions X_train dataset:", X_train.shape)