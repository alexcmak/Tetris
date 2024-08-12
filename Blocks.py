from Block import Block
from Position import Position

# L Block has 4 occupied blocks and is contained in a 3x3 box
#                  this is state 0
#  [ ][ ][#]                    (0,2)
#  [#][#][#]       (1,0), (1,1) (1,2)
#  [ ][ ][ ]       
class LBlock(Block):
	def __init__(self):
		super().__init__(id = 1)
		self.cells = { 
			0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)], # state 0
			1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
			3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}
		self.move(0,3) # so always appear in top middle


# J Block has 4 occupied blocks and is contained in a 3x3 box
#                  this is state 0
#  [#][ ][ ]       (0,0)
#  [#][#][#]       (1,0), (1,1) (1,2)
#  [ ][ ][ ]     

#                  this is state 1
#  [ ][#][#]              (0,1), (0,2)
#  [ ][#][ ]              (1,1)
#  [ ][#][ ]              (2,1)

class JBlock(Block):
	def __init__(self):
		super().__init__(id = 2)
		self.cells = { 
			0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
			3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
		}
		self.move(0,3)

# I Block has 4 occupied blocks and is contained in a 4x4 box
#                  this is state 0
#  [ ][ ][ ][ ]     
#  [#][#][#][#]     (1,0),(1,1) (1,2)(1,3)
#  [ ][ ][ ][ ] 
#  [ ][ ][ ][ ] 

class IBlock(Block):
	def __init__(self):
		super().__init__(id = 3)
		self.cells = {
			0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
			1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
			2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
			3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
		}
		self.move(-1,3) # so always appear in top middle

# O Block has 4 occupied blocks and is contained in a 2x2 box
class OBlock(Block):
	def __init__(self):
		super().__init__(id = 4)
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
			1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
			2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
			3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
		self.move(0,4)
  
# S Block has 4 occupied blocks and is contained in a 3x3 box
#                  this is state 0
#  [ ][#][#]              (0,1) (0,2)
#  [#][#][ ]       (1,0), (1,1) 
#  [ ][ ][ ]     

class SBlock(Block):
	def __init__(self):
		super().__init__(id = 5)
		self.cells = {
			0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
			1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
			2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
			3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
		}
		self.move(0,3)

# T Block has 4 occupied blocks and is contained in a 3x3 box
#                  this is state 0
#  [ ][#][ ]              (0,1) 
#  [#][#][#]       (1,0), (1,1) (1,2)
#  [ ][ ][ ]  

class TBlock(Block):
	def __init__(self):
		super().__init__(id = 6)
		self.cells = {
			0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
			3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
		}
		self.move(0,3)

# Z Block has 4 occupied blocks and is contained in a 3x3 box
#                  this is state 0
#  [#][#][ ]       (0,0), (0,1) 
#  [ ][#][#]              (1,1) (1,2)
#  [ ][ ][ ]  
class ZBlock(Block):
	def __init__(self):
		super().__init__(id = 7)
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
			1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
			3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
		}
		self.move(0,3)
