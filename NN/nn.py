import numpy as np 
import math
import scipy.special

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

        self.wih = np.random\
            .rand(self.inodes, self.hnodes)\
            * pow(self.inodes, -0.5)
        
        self.who = np.random\
            .rand(self.hnodes, self.onodes)\
            * pow(self.hnodes, -0.5)

        self.lr = learningrate

    def avtivate(self, x):
        return scipy.special.expit(x)

    def query(self, inputs):
        hidden_inputs = np.dot(inputs, self.wih)
        hidden_outputs = self.avtivate(hidden_inputs)

        final_inputs = np.dot(hidden_outputs, self.who)
        final_outputs = self.avtivate(final_inputs)

        return final_outputs

    def train(self, inputs, targets):
        hidden_inputs = np.dot(inputs, self.wih)
        hidden_outputs = self.avtivate(hidden_inputs)

        final_inputs = np.dot(hidden_outputs, self.who)
        final_outputs = self.avtivate(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = np.dot(output_errors, self.who.T)

        change= self.lr * np.dot(
            output_errors * final_outputs * (1.0 - final_outputs),
            hidden_outputs
        )

        print(np.shape(change))

def main():
    testing = np.load('Data/test.npy')[:,:-1]
    training = np.load('Data/train.npy')[:,:-1]
    testing_targets = np.load('Data/test.npy')[:,-1]
    training_targets = np.load('Data/train.npy')[:,-1]

    print(np.shape(testing))
    n = np.shape(testing)[1]
    nn = Net(n, 10, 1, 0.3)

    #nn.train(training, targets)

if __name__ == '__main__':
    main()