import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
from my_linear_regression import My_linear_regression as MLR

def add_polynomial_features(x, power):
    power = range(1, power + 1)
    init = x
    for pow in power:
        x = np.column_stack((x, init ** pow))
    return x

data = pd.read_csv("../resources/spacecraft_data.csv")
X = np.array(data[['Age','Thrust_power','Terameters']])
Y = np.array(data["Sell_price"])
LR = MLR(np.array([1.0, 1.0, 1.0, 1.0]))

print(LR.cost_function(LR.predict(X), Y))
LR.fit(X, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(X), Y))
P = add_polynomial_features(X, 2)
LR.theta = np.full(3 ** 2 + 1,1)
LR.fit(P, Y, alpha = 1e-9, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
mpl.plot(P, LR.predict(P), color='orange')
mpl.plot(P, Y)
mpl.show()
P = add_polynomial_features(X, 3)
LR.theta = np.full(10 + 3,1)
LR.fit(P, Y, alpha = 1e-12, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 4)
LR.theta = np.full(10 + 6,1)
LR.fit(P, Y, alpha = 1e-9, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 5)
LR.theta = np.full(10 + 9,1)
LR.fit(P, Y, alpha = 1e-9, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 6)
LR.theta = np.full(3 ** 6,1)
LR.fit(P, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 7)
LR.theta = np.full(3 ** 7 + 1,1)
LR.fit(P, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 8)
LR.theta = np.full(3 ** 8 + 1,1)
LR.fit(P, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 9)
LR.theta = np.full(3 ** 9 + 1,1)
LR.fit(P, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
P = add_polynomial_features(X, 10)
LR.theta = np.full(3 ** 10 + 1,1)
LR.fit(P, Y, alpha = 1e-5, max_iter = 5000000)
print(LR.cost_function(LR.predict(P), Y))
