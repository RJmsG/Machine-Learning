# Machine-Learning
Port of my machine learning scratch project to python.
Includes genetic algorithm.

## How to use:
First download nn.py from the repo.

It is simmilar to Tensorflow's Keras, so if you already understand that
it will be easy to use.

To setup your neural network, create your main python file and follow this example:

   from nn import Neural_Network

   ann = Neural_Network()

   ann.newlayer(1,0,1)

The function newlayer's arguments work like this:
(size, index, input)

More infromation can be found in nn.py and example.py
