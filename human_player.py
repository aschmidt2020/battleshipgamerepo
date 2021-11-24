from game_board import GameBoard
from player import Player
from human_board import HumanBoard

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
              
    def set_name(self):
        self.name = input('Please enter your name: ')
    
    def create_board(self):
        self.board = HumanBoard()
    
    def create_shooting_board(self):
        self.shooting_board = GameBoard()