from game_board import GameBoard

class Utilities:
    def display_instructions():
        print('\nINSTRUCTIONS: ')
        print('This is a two player battleship game. The game board is 20x20 (displayed below).')
        print('Each person has five ships (displayed below).')
        print("The game is a turn-based game that will continue until all of one person's ship are destoyed.")
        print('You can waste a turn by shooting at the same location, so pay attention!')
        print('Legend: (--) = open water, (SS) = ship placed, (S*) = ship hit, (xx) = miss')
        print('We will start by letting you place your ships.')
        print("Let's Begin!")
        print('*************************')

        game_board = GameBoard() #will display empty game board
        game_board.display_board()
        game_board.display_ships_to_place()