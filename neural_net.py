from __future__ import division

import math
import random
import sys

from data import generate_winnable_boards

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights,inputs):
    return sigmoid(dot(weights,inputs))

def feed_forward(neural_network, input_vector):
    outputs = []

    # process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias) for neuron in layer]
        outputs.append(output)

        input_vector = output

    return outputs

def backpropagate(network, input_vector, targets):
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target)
                    for output, target in zip(outputs, targets)]

    # adjust weights for output layer, one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # adjust the jth weight based on this neuron's delta and it's jth input
            output_neuron[j] -= output_deltas[i] * hidden_output

    # back-propagate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) * 
                    dot(output_deltas, [n[i] for n in output_layer])
                    for i, hidden_output in enumerate(hidden_outputs)]

    # adjust weights for hidden layer, one neuron at a time
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input

input_size = 9
num_hidden = 9
output_size = 9

# each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for _ in range(input_size + 1)]
                for _ in range(num_hidden)]

# each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for _ in range(num_hidden + 1)]
    for _ in range(output_size)]

# network starts with random weights
network = [hidden_layer, output_layer]

#data = generate_winnable_boards(400)

#inputs = [i[0] for i in data]
#targets = [[0]*9 for i in data]
inputs = []
targets = []

#for i in range(len(targets)):
#    targets[i][data[i][1]] = 1

def predict(input):
    output = feed_forward(network, input)[-1]
    return output.index(max(output))

examples = 250
iterations = 1000

for i in range(examples):
    new_board = []
    for j in range(9):
        new_board.append(random.choice([-1,1]))
    new_num = random.randint(0,8)
    new_board[new_num] = 0
    inputs.append(new_board)
    new_target = [0]*9
    new_target[new_num] = 1
    targets.append(new_target)

for _ in range(iterations):
    for input_vector, target_vector in zip(inputs, targets):
        backpropagate(network, input_vector, target_vector)
    if (_ % 20 == 0):
        print(str(int(_/iterations*100)) + '%')

total_correct = 0
for i in range(100000):
    new_board = []
    for j in range(9):
        new_board.append(random.choice([-1,1]))
    new_num = random.randint(0,8)
    new_board[new_num] = 0
    prediction = predict(new_board)
    if prediction == new_num:
        total_correct += 1
print(total_correct/100000)
