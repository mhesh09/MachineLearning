from cgi import test
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, LSTM 
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint

store_sales = pd.read_csv('train.csv')
# print(store_sales.head(10))

store_sales = store_sales.drop(['store','item'],axis='columns')
store_sales['date']= pd.to_datetime(store_sales['date'])

store_sales['date'] = store_sales['date'].dt.to_period('M')

monthly_sales = store_sales.groupby('date').sum().reset_index()




monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()

monthly_sales['sales_diff'] = monthly_sales['sales'].diff()


monthly_sales = monthly_sales.dropna()


supervised_data = monthly_sales.drop(['date','sales'],axis=1)



for i in range (1,13):
    col_name = 'month_'+str(i)
    supervised_data[col_name] = supervised_data['sales_diff'].shift(i)


supervised_data = supervised_data.dropna().reset_index(drop=True)



train_data = supervised_data[:-12]

test_data = supervised_data[-12:]
# print(test_data)

scaler = MinMaxScaler(feature_range=(-1,1))
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)



X_train, y_train = train_data[:,1:] , train_data[:,0:1]
X_test, y_test = test_data[:,1:], test_data[:,0:1]
y_train = y_train.ravel()
y_test = y_test.ravel()




sales_dates = monthly_sales['date'][-12:].reset_index(drop=True)
predict_df = pd.DataFrame(sales_dates)
act_sales = monthly_sales['sales'][-13:].to_list()


linreg_model = LinearRegression()
linreg_model.fit(X_train,y_train)
linreg_pred = linreg_model.predict(X_test)



linreg_pred = linreg_pred.reshape(-1,1)

linreg_pred_test_set = np.concatenate([linreg_pred, X_test],axis=1)



linreg_pred_test_set = scaler.inverse_transform(linreg_pred_test_set)



result_list = []
for index in range(0, len(linreg_pred_test_set)):
    result_list.append(linreg_pred_test_set[index][0] + act_sales[index])



linreg_pred_series = pd.Series(result_list,name='linreg_pred')


predict_df = predict_df.merge(linreg_pred_series,left_index=True,right_index=True)



linreg_rmse = np.sqrt(mean_squared_error(predict_df['linreg_pred'],monthly_sales['sales'][-12:]))
linreg_mae = mean_absolute_error(predict_df['linreg_pred'],monthly_sales['sales'][-12:])
linreg_r2 = r2_score(predict_df['linreg_pred'],monthly_sales['sales'][-12:])
print('Linear Regression RMSE: ', linreg_rmse)
print('Linear Regression MAE: ', linreg_mae)
print('Linear Regression R2 Score: ', linreg_r2)


xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.2,objective='reg:squarederror')
xgb_model.fit(X_train,y_train)
xgb_pred = xgb_model.predict(X_test)


xgb_pred = xgb_pred.reshape(-1,1)
xgb_pred_test_set = np.concatenate([xgb_pred,X_test],axis=1)
xgb_pred_test_set = scaler.inverse_transform(xgb_pred_test_set)

xgb_result_list = []
for index in range(0, len(xgb_pred_test_set)):
    xgb_result_list.append(xgb_pred_test_set[index][0] + act_sales[index])
xgb_pred_series = pd.Series(xgb_result_list,name='xgb_pred')
predict_df = predict_df.merge(xgb_pred_series,left_index=True,right_index=True)
print(predict_df)





# plt.figure(figsize=(15,5))
# plt.plot(monthly_sales['date'],monthly_sales['sales'])
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.title("Monthly Customer Sales")
# plt.show()

