from ship import Ship

class GameBoard:
    def __init__(self):
        self.board = [[]]
        self.create_board()
        print('\n')

        
        self.ships_list = []
        self.create_ships()
        

    def create_board(self):
        grid = [ ]
        rows, columns = (20, 20)
        
        for row in range(rows + 1):
            row = []
            for column in range(columns + 1):
                row.append('-- ')
            grid.append(row)
            
        self.board = grid
    
    def display_board(self):
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
        print('\nShips to place:')
        for ship in self.ships_list:
            print(f'{ship.name}, Size: {ship.size}')
        print('\n')
    
    def set_ship_places(self, ship, direction, row, column):
        ship_size = ship.size
        ship_direction = direction
        
        if self.board[row][column] == '-- ':
            if ship_direction == 'horizontal':
                for spot in range (ship_size):
                    self.board[row][column] = 'SS '
                    column = column + 1

            elif ship_direction == 'vertical':
                for spot in range(ship_size):
                    self.board[row][column] = 'SS '
                    row = row + 1
   
        else:
            print('Please available new row/column.')
    
        