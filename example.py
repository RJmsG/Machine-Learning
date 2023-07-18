from nn import Neural_Network

ann = Neural_Network()

ann.newlayer(2,0,2)
ann.newlayer(2,1,2)

x = ['0.1+0.2']
y = ['0.3+0.4']

print('finished setup, now training network')
ann.train(x,y,0.1)

print(f'OUTPUT:{ann.start([0.1])}')