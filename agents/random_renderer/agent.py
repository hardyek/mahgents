import time
import random

class Human():
    def __init__(self):
        pass

    def make_discard(self,observations,player):
        print(f"Player {player}")
        pile,hand,exposed,specials,wind = observations
        # processing ...
        print(f"Discard tile: {hand} : ")
        time.sleep(0.25)
        action = random.randint(0,13)
        print(f"Discard action made: {action}")
        time.sleep(0.25)
        return action

    def make_pong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        print(f"Pong: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action
    
    def make_kong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        print(f"Kong: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action

    def make_chow(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        print(f"Chow: {pile[-1], hand} : ")
        time.sleep(0.25)
        action = random.randint(0,1)
        print(f"Pickup action made: {action}")
        time.sleep(0.25)
        return action

    def make_pickup(self,item,observations,player):
        print(f"Player {player}")
        if item[1] == 0: # Pong
            return self.make_pong(observations)
        elif item[1] == 1: # Kong
            return self.make_kong(observations)
        elif item[1] == 2: # Chow
            return self.make_chow(observations)
