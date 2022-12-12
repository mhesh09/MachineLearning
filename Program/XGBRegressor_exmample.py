from numpy import absolute
from pandas import read_csv
from matplotlib import pyplot
import xgboost as xg
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score

url= 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
dataframe = read_csv(url, header=None)

X, y = dataframe.iloc[:,:-1], dataframe.iloc[:,-1]


model = xg.XGBRegressor()

#define evaluation method
cv = RepeatedKFold(n_splits=10,n_repeats=3,random_state=1)
#evaluation model
scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)

scores = absolute(scores)
print(scores)
print('Mean MAE: %.3f (%.3f)' % (scores.mean(), scores.std()))