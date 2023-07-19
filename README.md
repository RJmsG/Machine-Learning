# Machine-Learning
Port of my machine learning scratch project to python.
Includes genetic algorithm.

## How to use:
First download the folder named "pynn".

It is simmilar to Tensorflow's Keras, so if you already understand that
it will be easy to use.

To setup your neural network, create your main python file and follow this example:

   from pynn import Neural_Network

   ann = Neural_Network()

   ann.newlayer(1,1)
   
   ann.newlayer(2)

The function newlayer's arguments work like this:
(size, input-size) input-size is used for how much the network takes in. it does not need to be used more than once

More infromation can be found in nn.py and example.py
