from human_player import HumanPlayer
from game_board import GameBoard
import random
from computer_player import ComputerPlayer

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
        num_players_valid = False
        
        while num_players_valid == False:
            num_players = int(input('How many players? (1 or 2): '))
        
            if num_players == 2:
                print('\nPlayer One -->')
                self.player_one = HumanPlayer()
                
                print('Player Two -->')
                self.player_two = HumanPlayer()
                
                num_players_valid = True
                
            elif num_players == 1:
                print('\nPlayer One -->')
                self.player_one = HumanPlayer()
                
                #getting computer player
                self.player_two = ComputerPlayer()
                
                num_players_valid = True
        
        print('\nCurrent players: ')
        print(f'Player One Name: {self.player_one.name}')
        print(f'Player Two Name: {self.player_two.name}')
    
        return num_players
    
    def run_game(self):
        num_players = self.get_players()

        if num_players == 2:
            self.create_game_boards()
            self.create_player_board_p1()
            print(f'\n{self.player_one.name} here is your board:')
            self.player_one.board.display_board()
            
            self.create_player_board_p2()
            print(f'\n{self.player_two.name} here is your board:')
            self.player_two.board.display_board()
            
            self.shoot_cannon_two_players()
        elif num_players == 1:
            self.create_game_boards()
            self.create_player_board_p1()
            self.create_player_board_p2()
            self.shoot_cannon_one_player()
            
        self.display_winner()
        
    def create_game_boards(self): #game boards are used to attack and keep track of where you shot, player board are used to track your own ships
        self.game_board_p1 = GameBoard()
        self.game_board_p2 = GameBoard()
        
    def create_player_board_p1(self): 
        print(f'{self.player_one.name}, please place all ships -->')
        self.player_one.board.place_all_ships()
    
        print('\nPlayer 1 Board Completed\n')
        print('*************************')

    def create_player_board_p2(self):
        print(f'{self.player_two.name}, please place all ships --> ')
        self.player_two.board.place_all_ships()
        
        print('\nPlayer 2 Board Completed\n')
        print('*************************') 
    
    def shoot_cannon_two_players(self):
        bool_list = [True, False]
        player_one_turn = random.choice(bool_list)
        
        while len(self.player_one.board.ships_locations) > 0 and len(self.player_two.board.ships_locations) > 0:
            if player_one_turn == True:
                print(f'\n{self.player_one.name}')
                print('Here is your board -->')
                self.player_one.board.display_board()
                
                print('Here is your shooting board -->')
                self.game_board_p1.display_board()
                
                row = self.validate_shoot_cannon_row(input('Player One, please input a row number: '))
                column = self.validate_shoot_cannon_col(input('Player One, pease input a column number: '))
            
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
                
                row = self.validate_shoot_cannon_row(input('Player Two, please input a row number: '))
                column = self.validate_shoot_cannon_col(input('Player Two, please input a column number: '))
             
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
    
    #TODO look into clearing console to prevent seeing history
    
    def shoot_cannon_one_player(self):
        bool_list = [True, False]
        player_one_turn = random.choice(bool_list)
        
        while len(self.player_one.board.ships_locations) > 0 and len(self.player_two.board.ships_locations) > 0:
            if player_one_turn == True:
                print(f'\n{self.player_one.name}')
                print('Here is your board -->')
                self.player_one.board.display_board()
                
                print('Here is your shooting board -->')
                self.game_board_p1.display_board()
                
                row = self.validate_shoot_cannon_row(input('Player One, please input a row number: '))
                column = self.validate_shoot_cannon_col(input('Player One, please input a column number: '))
                
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
                print('Player Two Board Hidden')
                #self.player_two.board.display_board() #used to double check board is importing correctly
                
                print('Player Two Shooting Board Hidden')
                #self.game_board_p2.display_board() #used to double check board is importing correctly
                
                row = random.randint(1, 20)
                column = random.randint(0, 20)
                
                print(f'Computer player shooting at row: {row} and column: {column}...')
             
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
                
    def validate_shoot_cannon_row(self, number):
        try:
            number_value = int(number)
            if number_value > 20 or number_value < 1:
                raise Exception('Out of Shooting Range')
            elif number == '':
                raise ValueError
            else:
                return number_value
        except Exception as err:
            print(err)
            row = int(input('Please input a new row number: '))
            while row > 20 or row < 1 or row == '':
                print('Out of Shooting Range')
                row = int(input('Please input a new row number: '))
            return row
        except ValueError as err:
            print(err)
            row = int(input('Please input a new row number: '))
            while row > 20 or row < 1 or row == '':
                print('Out of Shooting Range')
                row = int(input('Please input a new row number: '))
            return row
        
    def validate_shoot_cannon_col (self, number):
        try:
            number_value = int(number)
            if number_value > 20 or number_value < 0:
                raise Exception('Out of Shooting Range')
            elif number_value == '':
                raise ValueError
            else:
                return number_value
        except Exception as err:
            print(err)
            column = int(input('Please input a new column: '))
            while column > 20 or column < 0 or column == '':
                print('Out of Shooting Range')
                column = int(input('Please input a new column: '))
            return  column
        except ValueError as err:
            print(err)
            column = int(input('Please input a new column: '))
            while column > 20 or column < 0 or column == '':
                print('Out of Shooting Range')
                column = int(input('Please input a new column: '))
            return  column
            
    def display_winner(self):
        if len(self.player_one.board.ships_locations) == 0:
            print(f"\nAll of Player One's ships have been destroyed. {self.player_two.name}, you win the game!")
            
        if len(self.player_two.board.ships_locations) == 0:
            print(f"\nAll of Player Two's ships have been destroyed. {self.player_one.name}, you win the game!")
            