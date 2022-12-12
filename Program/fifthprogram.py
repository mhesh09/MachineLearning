import pandas as pd
from sklearn.preprocessing import OneHotEncoder


data= pd.read_csv("file:///home/cooldevil/Documents/MachineLearning/Program/employee_data.csv")
# print(data.head())
# print(data['Gender'].value_counts())

# one_hot_encoded_data= pd.get_dummies(data, columns=["Remarks","Gender"])
# print(one_hot_encoded_data)

data['Gender'] = data['Gender'].astype('category')
data['Remarks']= data['Remarks'].astype('category')

data['new_Gen']= data['Gender'].cat.codes
data['new_Rem']= data['Remarks'].cat.codes

enc= OneHotEncoder()
enc_data = pd.DataFrame(enc.fit_transform(data[['new_Gen','new_Rem']]).toarray())
New_df = data.join(enc_data)

print(New_df)