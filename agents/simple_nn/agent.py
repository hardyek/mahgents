import torch

from models import DiscardModel, BinaryActionModel

class Agent():
    def __init__(self):
        self.discard_model = DiscardModel()
        self.pung_model = BinaryActionModel()
        self.gong_model = BinaryActionModel()
        self.seong_model = BinaryActionModel()

    def make_discard(self,observations,player):
        pile,hand,exposed,specials,wind = observations

        processed_hand = torch.tensor(hand, dtype=torch.float32)
        pile_history = torch.tensor(pile[-5:] if len(pile) >= 5 else pile + [0] * (5 - len(pile)), dtype=torch.float32)
        pile_length = torch.tensor([len(pile)], dtype=torch.float32)

        observation = torch.cat([processed_hand, pile_history, pile_length])

        probabilities = self.discard_model(observation)
        
        action = torch.argmax(probabilities).item()
        return action

    def make_pung(self,observations):
        pile,hand,exposed,specials,wind = observations

        processed_hand = torch.tensor(hand, dtype=torch.float32)
        takable = torch.tensor([pile[-1]], dtype=torch.float32)

        observation = torch.cat([processed_hand, takable])

        output = self.pung_model(observations)

        action = output.item() > 0.5
        return action
    
    def make_gong(self,observations):
        pile,hand,exposed,specials,wind = observations

        processed_hand = torch.tensor(hand, dtype=torch.float32)
        takable = torch.tensor([pile[-1]], dtype=torch.float32)

        observation = torch.cat([processed_hand, takable])

        output = self.gong_model(observations)

        action = output.item() > 0.5
        return action

    def make_soeng(self,observations):
        pile,hand,exposed,specials,wind = observations
        
        processed_hand = torch.tensor(hand, dtype=torch.float32)
        takable = torch.tensor([pile[-1]], dtype=torch.float32)

        observation = torch.cat([processed_hand, takable])

        output = self.gong_model(observations)

        action = output.item() > 0.5
        return action

    def make_pickup(self,item,observations,player):
        if item[1] == 0: # Pung
            action = self.make_pung(observations)
        elif item[1] == 1: # Gong
            action = self.make_gong(observations)
        elif item[1] == 2: # Soeng
            action = self.make_soeng(observations)
        return action