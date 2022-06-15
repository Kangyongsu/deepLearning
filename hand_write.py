import sys
sys.path.append("C:/Users/fgb/Desktop/deepLearning/deep-learning-from-scratch/dataset") # 부모 디렉토리의 파일을 가져올 수 있도록 설정
from dataset.mnist import load_mnist

(x_train ,t_train), (x_test,t_test)= \
    load_mnist(flatten=True, normalize =False)
    
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)