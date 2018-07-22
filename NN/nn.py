import numpy as np 
import math
import scipy

test = np.load('Data/test.npy')
train = np.load('Data/train.npy')

print(np.shape(test))
print(np.shape(train))

class Net:
    def __init__(
        self,
        inputnodes,
        hiddennodes,
        outputnodes,
        learningrate
    ):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = np.random.normal(
            0.5,
            pow(self.inodes, -0.5),
            (self.inodes, self.hnodes)
        )
        self.ho = np.random.normal(
            0.5,
            pow(self.hnodes, -0.5),
            (self.hnodes, self.onodes)
        )

        self.lr = learningrate

    def avtivate(self, x):
        return scipy.special.expit(x)
