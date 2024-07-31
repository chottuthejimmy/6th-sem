# Implement the non-parametric Locally Weighted Regression algorithm in order to fit data points. 
# Select appropriate data set for your experiment and draw graphs.

import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = [1, x0]
    X = [[1, i] for i in X]
    # X = np.array(X)
    xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau ** 2))
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    return x0 @ beta  # need to multiply by x0 to get the value of the function at x0

def draw(tau):
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plt.plot(X, Y, 'o', color='black')
    plt.plot(domain, prediction, color='red')
    plt.legend(['Data', 'Prediction'])
    plt.show()

X = np.linspace(-3, 3, num=1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + .5)

draw(10)
draw(0.1)
draw(0.01)
draw(0.001)