from Grid import Grid
from Blocks import *
import random
import pygame

class Game:
	def __init__(self, rows, cols):
		self.Cols = cols
		self.grid = Grid(rows,cols)
		self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0
	

	def update_score(self, lines_cleared, move_down_points):
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points

	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock()]

		block = random.choice(self.blocks)

		# center based on width and cols
		block.center(self.Cols)
		

		self.blocks.remove(block)
		return block
	
	def move_left(self):
		self.current_block.move(0, -1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	def move_down(self):
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()

	def lock_block(self):
		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			# print(position)
			self.grid.grid[position.row][position.column] = self.current_block.id
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		rows_cleared = self.grid.clear_full_rows()
		self.update_score(rows_cleared, 0)
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		self.grid.reset()
		self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0

	def block_fits(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True

	def rotate(self):
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()

	def block_inside(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True


	def draw(self, screen, game_over):
		offset = 11
		self.grid.draw(screen, offset, game_over)
		self.current_block.draw(screen, offset, offset) # shifted for scoreboard

		# draw to the Next Block
		if self.next_block.id == 3:
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 255, 280)
		else:
			self.next_block.draw(screen, 270, 270)

	
