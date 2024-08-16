import pygame, sys

from Grid import Grid
from Blocks import *
from Game import Game
from Colors import Colors

# Alex Mak
# based on tutorial from 'Programming with Nick'
# 8/9/2024

pygame.init()
title_font = pygame.font.Font(None, 40) # default font
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris Clone")

clock = pygame.time.Clock()

game = Game(20, 10)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)  # n miliseconds

def main():

	paused = False

	while True:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p and game.game_over == False: # P for pause
					paused = not paused	
				if event.key == pygame.K_n:  # N for new game
					if game.game_over == True:
						game.game_over = False
						game.reset()


				if not paused:

					if game.game_over == False:
						if event.key == pygame.K_LEFT:
							game.move_left()
						if event.key == pygame.K_RIGHT:
							game.move_right()
						if event.key == pygame.K_DOWN:
							game.move_down()
							game.update_score(0, 1)
						if event.key == pygame.K_UP:
							game.rotate()
						if event.key == pygame.K_SPACE:
							game.drop()
			
			if event.type == GAME_UPDATE and game.game_over == False and not paused:
				game.move_down()


		if not paused:

			score_value_surface = title_font.render(str(game.score), True, Colors.white)
			screen.fill(Colors.dark_blue)
			screen.blit(score_surface, (365, 20, 50, 50)) # block transfer
			screen.blit(next_surface, (375, 180, 50, 50)) # block transfer

			if game.game_over == True:
				screen.blit(game_over_surface, (320, 450, 50, 50)) # block transfer

			pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
			screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
			centery = score_rect.centery))
			pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
			game.draw(screen, game.game_over)


			pygame.display.update()
			clock.tick(60)
	

if __name__ == "__main__":
    main()
