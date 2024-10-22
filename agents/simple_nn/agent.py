import torch
import torch.nn as nn

class BinaryModel(nn.Module):
    def __init__(self):
        super(BinaryModel, self).__init__()

        self.input = nn.Linear(100,100)
        self.fc1 = nn.Linear(100,50)
        self.fc2 = nn.Linear(50,50)
        self.fc3 = nn.Linear(50,10)
        self.out = nn.Linear(10,1)

    def forward(self, x):
        x = nn.ReLU(self.input(x))
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc2(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.out(x)

class Agent():
    def __init__(self):

        pass

    def make_discard(self,observations,player):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = ...
        return action

    def make_pong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = ...
        return action
    
    def make_kong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = ...
        return action

    def make_chow(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = ...
        return action

    def make_pickup(self,item,observations,player):
        if item[1] == 0: # Pong
            action = self.make_pong(observations)
        elif item[1] == 1: # Kong
            action = self.make_kong(observations)
        elif item[1] == 2: # Chow
            action = self.make_chow(observations)
        return action