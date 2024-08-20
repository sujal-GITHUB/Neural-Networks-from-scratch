import numpy as np
import math

# One hot Encoding
# classes: 3
# Label: 0
# One-hot: [1, 0, 0]
# Prediction: [0.7, 0.1, 0.2]

# L = -(1*log(0.7) + 0*log(0.1) + 0*log(0.2))

softmax_output = np.array([[0.7, 0.1, 0.2],
                           [0.1, 0.5, 0.4],
                           [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1]

print(softmax_output[[0,1,2], class_targets])