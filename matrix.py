import numpy as np

a= [[1,2],[3,4],[5,6]]
b= [7,8]

print(np.shape(a))
print(np.shape(b))
print(np.dot(a,b))

a= [[1.0,0.5]]
b= [[0.1,0.3,0.5],[0.2,0.4,0.6]]

print(np.shape(np.dot(a,b)))
