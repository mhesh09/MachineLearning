import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


value1= abs(np.random.normal(1, 12,10))
value2 = abs(np.random.normal(2,3,100))
value3 = abs(np.random.normal(3,4,100))
value4 = abs(np.random.normal(10,15,100))

# x= np.c_[value1,value2,value3,value4]

print(value1)

# y = [int(np.random.randint(0,4)) for i in range(100)]

# data = pd.DataFrame()

# data['col1'] = value1
# data['col2'] = value2
# data['col3'] = value3
# data['col4'] = value4

# print(data)

# plt.subplot(2,2,1)
# plt.title('col1')
# plt.scatter(y,value1,color='r',label='col1')

# plt.savefig('data_visualization.jpg')
# plt.show()