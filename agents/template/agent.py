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