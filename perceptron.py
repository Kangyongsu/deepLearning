import numpy as np

# implement perceptron
# AND logic circuit
#x is signal
#w is weight
#AND circuit

def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if(tmp >= theta): 
        return 1
    else:
        return 0
    
print(f'AND(0,0) = {AND(0,0)}')
print(f'AND(1,0) = {AND(1,0)}')
print(f'AND(0,1) = {AND(0,1)}')
print(f'AND(1,1) = {AND(1,1)}\n')

#perceptron

# x1*w1 + x2*x2 <= 𝜽 (0) 
# x1*w1 + x2*x2 > 𝜽 (1) 
# Convert the above formula to the below formula
# x1*w1 + x2*x2 - 𝜽 <= 0 (0) 
# x1*w1 + x2*x2 - 𝜽 > 0 (1) 

def NAND(x1,x2):
    x= np.array([x1,x2]) # input
    y= np.array([-0.5,-0.5]) #weight
    b= 0.7 #bias
    tmp = np.sum(x*y) + b
    result = tmp
    if(result<=0):
        return 0
    else:
        return 1
    
print(f'NAND(0,0) = {NAND(0,0)}')
print(f'NAND(1,0) = {NAND(1,0)}')
print(f'NAND(0,1) = {NAND(0,1)}')
print(f'NAND(1,1) = {NAND(1,1)}\n')

def OR(x1,x2):
    x= np.array([x1,x2]) # input
    y= np.array([0.5,0.5]) #weight
    b= -0.3 #bias
    tmp = np.sum(x*y) + b
    result = tmp
    if(result<=0):
        return 0
    else:
        return 1
    
print(f'OR(0,0) = {OR(0,0)}')
print(f'OR(1,0) = {OR(1,0)}')
print(f'OR(0,1) = {OR(0,1)}')
print(f'OR(1,1) = {OR(1,1)}\n')

# The result of the perceptron is that the expression is the same, but it comes from the difference between w and b.

#XOR perceptron

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(f'XOR(0,0) = {XOR(0,0)}')
print(f'XOR(1,0) = {XOR(1,0)}')
print(f'XOR(0,1) = {XOR(0,1)}')
print(f'XOR(1,1) = {XOR(1,1)}')
