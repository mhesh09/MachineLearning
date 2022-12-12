import numpy as np

np.random.seed(0)

x1 = np.arange(10)
x2 = np.random.randint(10,high=None,size=(3,4))
x3 = np.random.randint(10,size=(3,4))

y1 = np.array([1,2,3])

print(y1)

print(y1.size,"\n")

print(y1.reshape(-1,1),"\n")

print(y1[np.newaxis,:], "\n")


# print("dimension is",x1.ndim,"\n shape is", x1.shape,"\n size is",x1.size);