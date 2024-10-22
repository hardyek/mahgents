import time
import random

class Random():
    def __init__(self):
        pass

    def make_discard(self,observations,player):
        print(f"DISCARD Player {player}")
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = random.randint(0,(len(hand)-1))
        return action

    def make_pung(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        action = random.randint(0,1)
        return action
    
    def make_gong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = random.randint(0,1)
        return action

    def make_soeng(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        action = random.randint(0,1)
        return action

    def make_pickup(self,item,observations,player):
        print(f"PICKUP  Player {player}")
        if item[1] == 0: # Pung
            return self.make_pung(observations)
        elif item[1] == 1: # Gong
            return self.make_gong(observations)
        elif item[1] == 2: # Soeng
            return self.make_soeng(observations)
