from player import Player
from human_board import HumanBoard

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
              
    def set_name(self):
        self.name = input('Please enter your name: ')
    
    def create_board(self):
        self.board = HumanBoard()