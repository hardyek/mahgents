from mahgym.game import MahjongGame
from mahgym.renderer import MahjongRenderer
import pygame

from agents.human.agent import Human

agent_array = [Human(),Human(),Human(),Human()]

renderer = MahjongRenderer()
game = MahjongGame(agent_array)
game.initialise_game()

clock = pygame.time.Clock()

renderer.render_game(game)

winner = game.game_loop_rendered(renderer,clock)

print(f"Player {winner} has won.")

pygame.quit()  