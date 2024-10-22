import torch
import torch.nn as nn

"""
simple_nn
Cut down the observation space to just the most relevant information,
this means that for the binary action spaces (pickups) the observation space is:

    hand - 13 tiles in the players hand
    takable (pile[-1]) - The tile the player can pick up

    Overall observation space is 14 integers

For the discard action space the observation space is just

    hand - 14 tiles in the players hand
    pile[:-5] - the last 5 items placed into the pile
    len(pile) - the length (size) of the pile

    Overall observation space is 20 integers
"""

class BinaryActionModel(nn.Module):
    def __init__(self):
        super(BinaryActionModel, self).__init__()

        self.input = nn.Linear(14,20)
        self.fc1 = nn.Linear(20,20)
        self.fc2 = nn.Linear(20,10)
        self.out = nn.Linear(10,1)

    def forward(self, x):
        x = nn.ReLU(self.input(x))
        x = nn.ReLU(self.fc1(x))
        x = nn.ReLU(self.fc2(x))
        x = nn.ReLU(self.fc2(x))
        x = nn.ReLU(self.fc2(x))
        x = nn.Sigmoid(self.out(x))

class DiscardModel(nn.Module):
    def __init__(self):
        super(DiscardModel, self).__init__()
        

class Agent():
    def __init__(self):

        pass

    def make_discard(self,observations,player):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = ...
        return action

    def make_pung(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = ...
        return action
    
    def make_gong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = ...
        return action

    def make_soeng(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = ...
        return action

    def make_pickup(self,item,observations,player):
        if item[1] == 0: # Pung
            action = self.make_pung(observations)
        elif item[1] == 1: # Gong
            action = self.make_gong(observations)
        elif item[1] == 2: # Soeng
            action = self.make_soeng(observations)
        return action