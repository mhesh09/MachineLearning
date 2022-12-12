import numpy as np 


x = np.array([[1,2],[3,4]]);
y = np.array([[5,6],[7,8]]);
z = np.array([[1,2,3],[4,5,6],[7,8,9]])




v = np.array([9,10])
w = np.array([11,12])

test = z[:,:-1]
print(test, "\n")

anothertest = z[:,-1]
print(anothertest,"\n")

print(x, "\n");
print(np.dot(v,w),"\n")