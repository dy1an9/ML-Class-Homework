import test_data1
import training_data1
import network

training_data = training_data1.training_data1
test_data = test_data1.test_data1
net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)