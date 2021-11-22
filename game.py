from human_player import HumanPlayer
from game_board import GameBoard
import random

#LEGEND
# '--' = open water
#'SS' = ship placed
#'S*' = ship hit
#'xx' = miss

class PlayGame:
    def __init__(self):
        self.display_instructions()
        self.player_one = '' #get player names
        self.player_two = ''
        self.get_players()

        
    def display_instructions(self):
        print('\nINSTRUCTIONS: ')
        print('This is a two player battleship game. The game board is 20x20 (displayed below).')
        print('Each person has five ships (displayed below).')
        print("The game is a turn-based game that will continue until all of one person's ship are destoyed.")
        print('You can waste a turn by shooting at the same location, so pay attention!')
        print('Legend: (--) = open water, (SS) = ship placed, (S*) = ship hit, (xx) = miss')
        print('We will start by letting you place your ships.')
        print("Let's Begin!")
        print('*************************')
    
        self.game_board = GameBoard() #will display empty game board
        self.game_board.display_board()
        self.game_board.display_ships_to_place()
        
    def get_players(self): #get player names and display current players
        print('\nPlayer One -->')
        self.player_one = HumanPlayer()
        
        print('Player Two -->')
        self.player_two = HumanPlayer()
        
        print('\nCurrent players: ')
        print(f'Player One Name: {self.player_one.name}')
        print(f'Player Two Name: {self.player_two.name}')
                
    def run_game(self):
        self.create_game_boards()
        self.create_player_board_p1()
        self.create_player_board_p2()
        self.shoot_cannon()
        self.display_winner()
        
    def create_game_boards(self): #game boards are used to attack and keep track of where you shot, player board are used to track your own ships
        self.game_board_p1 = GameBoard()
        self.game_board_p2 = GameBoard()
        
    def create_player_board_p1(self): 
        #order of ship placement: destroyer (size 2), submarine (size 3), battleship one (size 4), battleship 2 (size 4), aircraft (size 5)
        print(f'{self.player_one.name}, please place all ships -->')
        self.player_one.board.place_all_ships()
        
        print(f'\n{self.player_one.name} here is your board:')
        self.player_one.board.display_board()
        
        print('\nPlayer 1 Board Completed\n')
        print('*************************')
    
    
    def create_player_board_p2(self):
        
        print(f'{self.player_two.name}, please place all ships --> ')
        self.player_two.board.place_all_ships()
        
        print(f'\n{self.player_two.name} here is your board:')
        self.player_two.board.display_board()
        
        print('\nPlayer 2 Board Completed\n')
        print('*************************') 
    
        
    def shoot_cannon(self):
        bool_list = [True, False]
        player_one_turn = random.choice(bool_list)
        
        while len(self.player_one.board.ships_locations) > 0 and len(self.player_two.board.ships_locations) > 0:
        
            if player_one_turn == True:
                print(f'\n{self.player_one.name}')
                print('Here is your board -->')
                self.player_one.board.display_board()
                
                print('Here is your shooting board -->')
                self.game_board_p1.display_board()
                
                row = int(input('Player 1, please input a row number: '))
                column = int(input('Player 1, please input a column number: '))
            
                if self.player_two.board.board[row][column] == '-- ':
                    print('Nothing but ocean here!\n')
                    self.player_two.board.board[row][column] = 'xx '
                    self.game_board_p1.board[row][column] = 'xx '
                elif self.player_two.board.board[row][column] == 'SS ':
                    print('You hit a ship!\n')
                    self.player_two.board.board[row][column] = 'S* '
                    self.game_board_p1.board[row][column] = 'S* '
                    self.player_two.board.locate_ship(row, column)
                
                player_one_turn = not player_one_turn
        
            elif player_one_turn == False:
                print(f'\n{self.player_two.name}')
                print('Here is your board -->')
                self.player_two.board.display_board()
                
                print('Here is your shooting board -->')
                self.game_board_p2.display_board()
                
                row = int(input('Player 2, please input a row number: '))
                column = int(input('Player 2, please input a column number: '))
             
                if self.player_one.board.board[row][column] == '-- ':
                    print('Nothing but ocean here!\n')
                    self.player_one.board.board[row][column] = 'xx '
                    self.game_board_p2.board[row][column] = 'xx '
                elif self.player_one.board.board[row][column] == 'SS ':
                    print('You hit a ship!\n')
                    self.player_one.board.board[row][column] = 'S* '
                    self.game_board_p2.board[row][column] = 'S* '
                    self.player_one.board.locate_ship(row, column)
        
                player_one_turn = not player_one_turn
    
    def display_winner(self):
        if len(self.player_one.board.ships_locations) == 0:
            print(f"\nAll of Player One's ships have been destroyed. {self.player_two.name}, you win the game!")
            
        if len(self.player_two.board.ships_locations) == 0:
            print(f"\nAll of Player Two's ships have been destroyed. {self.player_one.name}, you win the game!")
            