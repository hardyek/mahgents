class Agent():
    def __init__(self):
        pass

    def make_discard(self,observations):
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

    def make_pickup(self,item,observations):
        if item[1] == 0: # Pong
            self.make_pong(observations)
        elif item[1] == 1: # Kong
            self.make_kong(observations)
        elif item[1] == 2: # Chow
            self.make_chow(observations)