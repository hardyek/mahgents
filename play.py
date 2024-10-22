from mahgym.game import MahjongGame
from mahgym.renderer import MahjongRenderer
import pygame

from agents.random.agent import Random 

agent_array = [Random(),Random(),Random(),Random()]

renderer = MahjongRenderer()
game = MahjongGame(agent_array)
game.initialise_game()

clock = pygame.time.Clock()

renderer.render_game(game)

winner, winning_hand = game.game_loop_rendered(renderer,clock)

print(f"Player {winner} has won.")
print(f"With hand : {winning_hand}")

pygame.quit()  