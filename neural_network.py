from matplotlib.pyplot import step, ylim
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=int)
    
x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt,ylim(-0.1,1.1)
plt.show()
     

def signoid(x):
    return 1/ (1+np.exp(-x))

x = np.arange(-5.0,5.0,0.1)
y = signoid(x)
plt.plot(x,y)
plt,ylim(-0.1,1.1)
plt.show()

 
