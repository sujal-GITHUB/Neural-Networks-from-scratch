import numpy as np
np.random.seed(0)

X = [[1, 2, 3, 2.5],[2, 5, -1, 2],[-1.5, 2.7, 3.3, -0.8]]
inputs = [0,2,-1,3.3,-2.7,1.1,2.2,-100]
outputs = []

#RELU
for i in inputs:
    if i>0:
        outputs.append(i)
    else:
        outputs.append(0)

#
#for i in inputs:
#    outputs.append(max(i,0))

print(outputs)