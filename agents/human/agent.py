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

    def make_pung(self,observations):
        pile,hand,exposed,specials,wind = observations
        # processing ...
        text = f"Pung: {pile[-1], hand} : "
        action = int(input(text))
        return action
    
    def make_gong(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        text = f"Gong: {pile[-1], hand} : "
        action = int(input(text))
        return action

    def make_soeng(self,observations):
        pile,hand,exposed,specials,wind = observations
        # Processing
        text = f"Soeng: {pile[-1], hand} : "
        action = int(input(text))
        return action

    def make_pickup(self,item,observations,player):
        print(f"Player {player}")
        if item[1] == 0: # Pung
            return self.make_pung(observations)
        elif item[1] == 1: # Gong
            return self.make_gong(observations)
        elif item[1] == 2: # Soeng
            return self.make_soeng(observations)
