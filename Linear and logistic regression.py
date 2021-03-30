过没有？这个需要准备吗？对DS

63垅YZDH
2021-2-14 01:00:29
本帖最后由 YZDH 于 2021-2-14 09:06 编辑
引用: czhmily 发表于 2021-2-14 08:08
关于 机器学习算法实现，我看LZ已经给出了KNN KMEANS 请问其他的例如logistic regression, decision tree  ...

Logistic Regression 和 Linear Regression肯定是要的。

Decision Tree我感觉可能pseudo code写不完面试考的可能性可能并不大。

但是我也会之后写一下，多准备总比不准备好。

64垅czhmily
2021-2-14 04:37:09
引用: YZDH 发表于 2021-2-14 09:00
Logistic Regression 和 Linear Regression肯定是要的。
. check 1point3acres for more.
Decision Tree我感觉可能pseudo code写不完面 ...

谢谢 期待LZ的update！

65垅YZDH
2021-2-17 00:19:09
29. Train Linear Regression and Logistic Regression by using gradient descent
参考
1. 斯坦福 CS229的Lecture Note: https://see.stanford.edu/materials/aimlcs229/cs229-notes1.pdf
2. Python Machine Learning的ch03 和 ch10的code: https://github.com/rasbt/python-machine-learning-book-3rd-edition


(1). Train Linear Regression

[mw_shl_code=python,true]import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt[/mw_shl_code]


[mw_shl_code=python,true]import numpy as np
. From 1point 3acres bbs
class Linear_Regression:
   
    # initialize learning_rate and iteration times
    def __init__(self, learning_rate=0.001, n_iter=50):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
   
    # fit the model
    def fit(self, X, y):
        # initialize w, the linear regression coefficients
        self.w = np.zeros(1 + X.shape[1]). From 1point 3acres bbs
        self.costs = []
        
        for i in range(self.n_iter):
            # calculate h(X)
            h_X = self.h(X)
            # calculate errors = y - h(X). From 1point 3acres bbs
            errors = (y - h_X)
            
            # update linear coefficients w[1:]
            self.w[1:] += self.learning_rate*np.dot(X.T, errors)
            # update intercept w[0]
            self.w[0] += self.learning_rate*errors.sum()
            # calculate the L2 cost: J
            J = (errors**2).sum()/2.0
            self.costs.append(J)
            
        return self
   
    # calculate h(x) = x^{T}*w, in matrix form: h(X) = X*w
    def h(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]
   
    # do prediction by using h(X) = X*w
    def predict(self, X):
        return self.h(X)[/mw_shl_code]


[mw_shl_code=python,true]df = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
                 'python-machine-learning-book-3rd-edition/'
                 'master/ch10/housing.data.txt',
                 header=None,
                 sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']


# get X, y
X = df[['RM']].values
y = df['MEDV'].values

# Standardize X, y
sc_x = StandardScaler()
sc_y = StandardScaler()

X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()

# Fit the model by using X_std and y_std
lr = Linear_Regression()
lr.fit(X_std, y_std)
. 1point3acres
print('Slope: %.3f' % lr.w[1])
print('Intercept: %.3f' % lr.w[0])

# Slope: 0.695
# Intercept: -0.000[/mw_shl_code]


(2). Train Logistic Regression

[mw_shl_code=python,true]class Logistic_Regression:-baidu 1point3acres
   
    # initialize learning_rate and iteration times and random seed for initial value of w
    # w is the logistic regression coefficients
    def __init__(self, learning_rate=0.05, n_iter=100, random_state=1):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.random_state = random_state
        
    def fit(self, X, y):
        # set random seed to a distribution from which an initial value for w is generated
        random_generator = np.random.RandomState(self.random_state)
        # initialize
        self.w = random_generator.normal(loc=0.0, scale=0.01, size=1 + X.shape[1]). From 1point 3acres bbs
        self.cost = []
        
        for i in range(self.n_iter):
            # calculate Z(X)
            Z_X = self.Z(X)
            # calculate h = g(Z)
            h_X = self.g(Z_X)
            # calculate errors = y - h(X)
            errors = (y - h_X)
            # update logistic regression coefficients w[1:]
            self.w[1:] += self.learning_rate*np.dot(X.T, errors)
            # update intercept w[0]
            self.w[0] += self.learning_rate*errors.sum()
            
            # calculate the cross-entropy cost
            cost = -y.dot(np.log(h_X)) - ((1 - y).dot(np.log(1 - h_X)))
            self.cost.append(cost)
   
    # calculate z = x^{T}*w, in matrix form: Z = X*w
    def Z(self, X):-baidu 1point3acres
        return self.w[0] + np.dot(X, self.w[1:])
   
    # calculate g(z), the sigmoid function
    def g(self, z):
        return 1.0/(1 + np.exp(-z))
   
    # make prediction for new X
    def predict(self, X):
        return np.where(self.Z(X) >= 0.0, 1, 0)
