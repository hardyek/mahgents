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
    pile[-5:] - the last 5 items placed into the pile
    len(pile) - the length (size) of the pile

    Overall observation space is 20 integers
"""

class BinaryActionModel(nn.Module):
    def __init__(self, dropout_rate=0.2):
        super(BinaryActionModel, self).__init__()
        
        self.input = nn.Linear(14, 20)
        self.bn1 = nn.BatchNorm1d(20)
        self.fc1 = nn.Linear(20, 20)
        self.bn2 = nn.BatchNorm1d(20)
        self.fc2 = nn.Linear(20, 10)
        self.bn3 = nn.BatchNorm1d(10)
        self.out = nn.Linear(10, 1)
        
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.bn1(self.input(x)))
        x = self.dropout(x)
        x = self.relu(self.bn2(self.fc1(x)))
        x = self.dropout(x)
        x = self.relu(self.bn3(self.fc2(x)))
        x = self.dropout(x)
        x = self.sigmoid(self.out(x))
        return x

class DiscardModel(nn.Module):
    def __init__(self, dropout_rate=0.2):
        super(DiscardModel, self).__init__()

        self.input = nn.Linear(20, 40)
        self.bn1 = nn.BatchNorm1d(40)
        self.fc1 = nn.Linear(40, 40)
        self.bn2 = nn.BatchNorm1d(40)
        self.fc2 = nn.Linear(40, 30)
        self.bn3 = nn.BatchNorm1d(30)
        self.out = nn.Linear(30, 14)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = self.relu(self.bn1(self.input(x)))
        x = self.dropout(x)
        x = self.relu(self.bn2(self.fc1(x)))
        x = self.dropout(x)
        x = self.relu(self.bn3(self.fc2(x)))
        x = self.dropout(x)
        x = self.softmax(self.out(x))
        return x