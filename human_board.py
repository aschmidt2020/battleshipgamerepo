from ship import Ship
from game_board import GameBoard
class HumanBoard(GameBoard): #inherit game_board
    def __init__(self):
        self.ships_locations = []
        super().__init__()

    def can_place_ship(self, ship, direction, row, column):
        can_place_ship = False
        ship_size = ship.size
        ship_direction = direction
        
        if ship_direction == 'h': #placing ship validation
            for spot in range(ship_size):
                if row > 20 or column > 20:
                    can_place_ship = False
                    break
                elif self.board[row][column] == '-- ':
                    column = column + 1
                    can_place_ship = True
                else:
                    can_place_ship = False
                    break
        
        elif ship_direction == 'v':
            for spot in range(ship_size):
                if row > 20 or column > 20:
                    can_place_ship = False
                    break
                elif self.board[row][column] == '-- ':
                    row = row + 1   
                    can_place_ship = True
                else:
                    can_place_ship = False
                    break

        return can_place_ship
    
    def set_ship_places(self, ship, direction, row, column):
        ship_size = ship.size
        ship_direction = direction
        can_place_ship = self.can_place_ship(ship, direction, row, column)
        
        while can_place_ship == False: 
            print('Space not available Please select another space-->')
            ship_direction = input('Please select horizontal or vertical (h/v): ')
            row = int(input('Please input a new row: '))
            column = int(input('Please input a new colum: '))
            
            can_place_ship = self.can_place_ship(ship, ship_direction, row, column)
            
        if can_place_ship == True:
            if ship_direction == 'h':
                start_row = row
                end_row = row
                start_column = column
                end_column = column + ship_size
                    
                for spot in range (ship_size):
                    self.board[row][column] = 'SS '
                    column = column + 1
                    
                self.ships_locations.append([start_row, end_row, start_column, end_column, ship_direction])

            elif ship_direction == 'v':
                start_row = row
                end_row = row + ship_size
                start_column = column
                end_column = column
                
                for spot in range(ship_size):
                    self.board[row][column] = 'SS '
                    row = row + 1
                
                self.ships_locations.append([start_row, end_row, start_column, end_column, ship_direction])
                

            can_place_ship = self.can_place_ship(ship, ship_direction, row, column)

    def place_all_ships(self):
        
        for ship in self.ships_list:
            print(f'\nPlease place {ship.name} (ship size: {ship.size}): ')
            
            ship_direction = input('Please select horizontal or vertical (h/v): ')
            
            if ship_direction == 'h' or ship_direction == 'v':
                row = int(input('Please input a row number: '))
                column = int(input('Please input a column number: '))
            else:
                while ship_direction != 'h' or ship_direction != 'v':
                    ship_direction = input('Please input another direction (h/v): ')
                    
                    if ship_direction == 'h' or ship_direction == 'v':
                        row = int(input('Please input a row number: '))
                        column = int(input('Please input a column number: '))
                    
                    break
        
            self.set_ship_places(ship, ship_direction, row, column) 

    
    def locate_ship(self, row, column):
        for x in range(5):
            start_row = self.ships_locations[x][0]
            end_row = self.ships_locations[x][1]
            start_column = self.ships_locations[x][2]
            end_column = self.ships_locations[x][3]
            ship_direction = self.ships_locations[x][4]
            
            if start_row <= row <= end_row and start_column <= column <= end_column: #used to locate ship in list of ships
                self.is_ship_eliminated(start_row, end_row, start_column, end_column, ship_direction)
                break

    def is_ship_eliminated(self, start_row, end_row, start_column, end_column, ship_direction):
        ship_eliminated = False
        
        if ship_direction == 'h':
            for column in range(start_column, end_column):
                if self.board[start_row][column] != 'S* ':
                    ship_eliminated = False
                    continue
                else:
                    ship_eliminated = True
        
        elif ship_direction == 'v':
            for row in range(start_row, end_row):
                if self.board[row][start_column] != 'S* ':
                    ship_eliminated = False
                    continue
                else:
                    ship_eliminated = True
                        
        if ship_eliminated == False:
            print('Ship not destroyed yet.\n')
            
        elif ship_eliminated == True:
            self.ships_locations.remove([start_row, end_row, start_column, end_column, ship_direction])
            print('Ship Destroyed!\n')

