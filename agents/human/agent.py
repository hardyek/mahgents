class Human():
    def __init__(self):
        pass

    def make_discard(self,observations,player):
        print(f"Player {player}")
        pile,hand,exposed,specials,wind = observations
        # processing ...
        text = f"Discard tile: {hand} : "
        action = int(input(text))
        return action

    def make_pong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        text = f"Pong: {pile[-1], hand} : "
        action = int(input(text))
        return action
    
    def make_kong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        text = f"Kong: {pile[-1], hand} : "
        action = int(input(text))
        return action

    def make_chow(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        text = f"Chow: {pile[-1], hand} : "
        action = int(input(text))
        return action

    def make_pickup(self,item,observations,player):
        print(f"Player {player}")
        if item[1] == 0: # Pong
            return self.make_pong(observations)
        elif item[1] == 1: # Kong
            return self.make_kong(observations)
        elif item[1] == 2: # Chow
            return self.make_chow(observations)
