import time
import random

class RandomRendered():
    def __init__(self):
        pass

    def make_discard(self,observations,player):
        print(f"Player {player}")
        pile,hand,exposed,specials,wind = observations
        # processing ...
        print(f"Discard tile: {hand} : ")
        time.sleep(0.25)
        action = random.randint(0,(len(hand)-1))
        print(f"Discard action made: {action}")
        time.sleep(0.25)
        return action

    def make_pung(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        print(f"Pung: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action
    
    def make_gong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        print(f"Gong: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action

    def make_soeng(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        print(f"Soeng: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action

    def make_pickup(self,item,observations,player):
        print(f"Player {player}")
        if item[1] == 0: # Pung
            return self.make_pung(observations)
        elif item[1] == 1: # Gong
            return self.make_gong(observations)
        elif item[1] == 2: # Soeng
            return self.make_soeng(observations)
