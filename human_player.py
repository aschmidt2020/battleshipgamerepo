from game_board import GameBoard
from player import Player
from human_board import HumanBoard

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
              
    def set_name(self):
        """sets player name equal to input"""
        self.name = input('Please enter your name: ')
    
    def create_board(self):
        """instantiates computer board that will allow person to set their ships"""
        self.board = HumanBoard()
    
    def create_shooting_board(self):
        """instantiates shooting board that is a blank board to record shots taken"""
        self.shooting_board = GameBoard()