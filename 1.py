import numpy as np
np.random.seed(0)

X = [[1, 2, 3, 2.5],[2, 5, -1, 2],[-1.5, 2.7, 3.3, -0.8]]

class Layer:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons));
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer(4,5)
layer2 = Layer(5,4)
layer3 = Layer(4,2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
layer3.forward(layer2.output)
print(layer3.output)