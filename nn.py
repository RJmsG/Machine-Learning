import numpy as np
from random import randint, choice

class Neural_Network():
    """This is my implementation of a neural network 'engine'. 
         It's not much different from others.
         However, it does have a feature for training that uses a version of the genetic algorithm.
         """

    def __init__(self):
        self.ws = []  # weights
        self.bs = []  # bias
        self.inp = [] # input
        self.out = [] # output
        self.leg = [] # length
        self.ids = [] # weight IDs
        #self.ly = 0
        self.r1 = 1
        self.r2 = 0
        self.g = 0  # generation
        self.lyr = 0  # layers

        self.td = []  # training data
        self.ans = [] # expected answers
        self.c1 = []
        self.c2 = []
    
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))
    
    def rnd(self): # random number between 0.00 and 1
        return randint(-100,100) * 0.01
    
    def fdif(self,a,b): # find difference between numbers
        c = 0
        if b < a:
            c = a - b
        elif b > a:
            c = b - a
        else: return 0

        if str(c)[0] == '-':
            c -= c * 2
        return c
    
    def check(self, exp):
        n = 0
        for i in range(len(exp)):
            n += self.fdif(self.out[i],float(exp[i]))
        return n

    def newlayer(self, sz,ly,inp):
        self.lyr+=1
        self.bs.append(self.rnd())
        c=0
        for cn in range(sz):
            for i in range(inp):
                self.ws.append(self.rnd())
                self.ids.append(f'{str(c)}+{ly}')
                c+=1
        self.leg.append(sz)
    
    def layer(self, ly, b):
        self.out = []
        c = 0
        for a in range(self.leg[ly]):
            o = 0
            for i in self.inp:
                o+=(self.ws[self.ids.index(f'{c}+{ly}')]+float(i))
                c+=1
            self.out.append(self.sigmoid(o+b))
    
    def start(self, x):
        self.inp = x
        for i in range(self.lyr):
            self.layer(i,self.bs[i-1])
            if 0 < len(self.out):
                self.inp = self.out
        return self.out
    
    def gen(self):
        self.c1 = self.ws
        self.c2 = []
        for i in self.ws:
            self.c2.append(i+self.rnd())
    
    def test(self):
        o = 0
        c = 0
        for i in self.td:
            self.start(i.split('+'))
            o+=self.check(self.ans[c].split('+'))
            c+=1
        return o
    
    def trial(self):
        self.ws = self.c1
        self.r1 = self.test()
        self.ws = self.c2
        self.r2 = self.test()
    
    def choose(self):
        if self.r1 < self.r2:
            self.ws = self.c1
        else:
            self.ws = self.c2
            self.g += 1
    
    def train(self, x, y, min):
        self.td = x
        self.ans = y
        self.g = 0
        self.r1 = 1
        c = min
        while c < self.r1:
            self.gen()
            self.trial()
            self.choose()