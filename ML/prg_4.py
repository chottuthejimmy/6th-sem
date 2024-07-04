# Build an Artificial Neural Network by implementing the Backpropagation algorithm 
# and test the same using appropriate data sets.

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = X / np.amax(X, axis=0)
y = y / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_gradient(x):
    return x * (1 - x)

epochs = 1000
lr = 0.2
inp = 2
hn = 3
on = 1

win = np.random.uniform(size=(inp, hn))
bh = np.random.uniform(size=(1, hn))
wout = np.random.uniform(size=(hn, on))
bo = np.random.uniform(size=(1, on))

for epoch in range(epochs):
    hin = np.dot(X, win) + bh
    hout = sigmoid(hin)
    oin = np.dot(hout, wout) + bo
    pred = sigmoid(oin)

    eout = y - pred
    gout = sigmoid_gradient(pred)
    dout = eout * gout

    eh = np.dot(dout, wout.T)
    gh = sigmoid_gradient(hout)
    dh = eh * gh

    wout += np.dot(hout.T, dout) * lr
    win += np.dot(X.T, dh) * lr

print("Normalized Input: \n" , str(X))
print("\nActual Output: \n" , str(y))
print("\nPredicted Output: \n" , str(pred))