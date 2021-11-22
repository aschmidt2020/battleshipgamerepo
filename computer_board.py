from ship import Ship
import random

class ComputerBoard:
    def __init__(self):
        self.board = [[]]
        self.create_board()
        print('\n')

        
        self.ships_list = []
        self.create_ships()
         
        self.ships_locations = []

    def create_board(self): #creates 20x20 game board
        grid = [ ]
        rows, columns = (20, 20)
        
        for row in range(rows + 1):
            row = []
            for column in range(columns + 1):
                row.append('-- ')
            grid.append(row)
            
        self.board = grid
    
    def display_board(self): #displays board with 00-20 on rows and columns
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
                
    def create_ships(self): #instantiates 5 ships
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
    
    def display_ships_to_place(self): #displays 5 ships and 
        print('\nShips to place:')
        for ship in self.ships_list:
            print(f'{ship.name}, Size: {ship.size}')
        print('\n')
    
    
    def can_place_ship(self, ship, direction, row, column):
        ship_size = ship.size
        ship_direction = direction
        can_place_ship = False
        
        
        if can_place_ship == False:
            if ship_direction == 'h': #placing ship validation
                for spot in range(ship_size):
                    if self.board[row][column] == '-- ':
                        column = column + 1
                        can_place_ship = True
                    else:
                        can_place_ship = False
                        break
         
            elif ship_direction == 'v':
                for spot in range(ship_size):
                    if self.board[row][column] == '-- ':
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
                
        while can_place_ship == False: 
            print('Space not available Please select another space-->')
            can_place_ship = self.can_place_ship(ship, input('Please select horizontal or vertical (h/v): '), int(input('Please input a new row: ')), int(input('Please input a new column: ')))

    def place_all_ships(self):
        ship_direction_list = ['h', 'v']
        
        for ship in self.ships_list:
            print(f'\nPlease place {ship.name} (ship size: {ship.size}): ')
            
            ship_direction = random.choice(ship_direction_list)
            row = random.randint(0, 20)
            column = random.randint(0, 20)
            

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

