from matplotlib.pyplot import step, ylim
import numpy as np
import matplotlib.pylab as plt

# def step_function(x):
#     return np.array(x>0,dtype=int)
    
# x = np.arange(-5.0,5.0,0.1)
# y = step_function(x)
# plt.plot(x,y)
# plt,ylim(-0.1,1.1)
# plt.show()
     

# def signoid(x):
#     return 1/ (1+np.exp(-x))

# x = np.arange(-5.0,5.0,0.1)
# y = signoid(x)
# plt.plot(x,y)
# plt,ylim(-0.1,1.1)
# plt.show()

# def relu(x):
#     return np.maximum(0,x)

# x = np.arange(-5.0,-0.1,0.1)
# y = relu(x)
# plt.plot(x,y)
# plt,ylim(-0.1,1.1)
# plt.show()

def softmax(x):
    c= np.max(x)
    exp_a = np.exp(x-c) # 오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y= exp_a / sum_exp_a
    
    return y
    
x = np.arange(-1010,-990,10)
print(x)
y = softmax(x)
print(np.sum(y))
plt.plot(x,y)
plt,ylim(-0.1,1.1)
plt.show()
    
