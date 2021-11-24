from ship import Ship

class GameBoard:
    def __init__(self):
        """creates 20x20 game board and creates 5 ships"""
        self.board = [[]]
        self.create_board()
        print('\n')

        
        self.ships_list = []
        self.create_ships()
        
    def create_board(self):
        """creates 20x20 game board"""
        grid = [ ]
        rows, columns = (20, 20)
        
        for row in range(rows + 1):
            row = []
            for column in range(columns + 1):
                row.append('-- ')
            grid.append(row)
            
        self.board = grid
    
    def display_board(self):
        """displays 20x20 game board with numbers along top and side"""
        rows, columns = (20, 20)
        
        for row in range(rows + 1):
            if 0 <= row <= 9:
                print(f'0{row}', '', end = ' ')
            else:
                print(row, '', end = ' ')
                
            for column in range(columns + 1):
                if row == 0:
                    if 0 <= column <= 9:
                        print(f'0{column}', ' ', end = '')
                    else:
                        print(column, '', end = ' ')
                else:
                    print(self.board[row][column], end = ' ')
            print()
      
    def create_ships(self):
        """instantiates 5 Ships"""
        destroyer = Ship(2, 'Destroyer') 
        submarine = Ship(3, 'Sub')
        battleship_one = Ship(4, 'Battleship 1')
        battleship_two = Ship(4, 'Battleship 2')
        aircraft = Ship(5, 'Aircraft Carrier')
        
        self.ships_list.append(destroyer)
        self.ships_list.append(submarine)
        self.ships_list.append(battleship_one)
        self.ships_list.append(battleship_two)
        self.ships_list.append(aircraft)
    
    def display_ships_to_place(self):
        """displays all 5 instantiated ships to place"""
        print('\nShips to place:')
        for ship in self.ships_list:
            print(f'{ship.name}, Size: {ship.size}')
        print('\n')
