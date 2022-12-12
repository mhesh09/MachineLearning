import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB


iris = datasets.load_iris()
print(iris)
X= iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

gnb = GaussianNB()

# train the model
gnb.fit(X_train, y_train)

# make predictions
gnb_pred = gnb.predict(X_test)
# print the accuracy
print("Accuracy of Gaussian Naive Bytes:", accuracy_score(y_test, gnb_pred))

#Support Vector Machine

svm_clf = svm.SVC(kernel='linear')
#train the model 
svm_clf.fit(X_train,y_train)
#make prediction
svm_clf_pred = svm_clf.predict(X_test)
#print the accuracy
print("Accuracy of Support Vector Machine:", accuracy_score(y_test, svm_clf_pred))


