from game_board import GameBoard
from player import Player
from computer_board import ComputerBoard
import random

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
              
    def set_name(self):
        """chooses computer name from  a list"""
        computer_name_list = ['William', 'Julia', 'George', 'Tom']
        self.name = random.choice(computer_name_list)
    
    def create_board(self):
        """instantiates computer board that will allow person to set their ships"""
        self.board = ComputerBoard()
    
    def create_shooting_board(self):
        """instantiates shooting board that is a blank board to record shots taken"""
        self.shooting_board = GameBoard()