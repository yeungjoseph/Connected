#Joseph Yeung 12752133

NONE = 0
WHITE = 1
BLACK = 2
pieces1 = {'.': NONE,'W': WHITE,'B': BLACK}

class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


class GameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass


class GameState:
    def __init__(self,first_move,win_rule,rows,cols):
        '''Creates an empty board w/ specified rows and cols'''
        self._winner = NONE

        self._gameover = False
        
        if win_rule != '>' and win_rule != '<':
            raise ValueError("win_rule must be '<' or '>'")
        self._win_rule = win_rule
        
        if first_move != 'W' and first_move != 'B':
            raise ValueError("first_move must be 'W' or 'B'")
        self._turn = pieces1[first_move]
        
        if not _number_is_valid(rows):
            raise ValueError(
                'rows must be an even integer between 4 and 16')
        self._rows = rows
        
        if not _number_is_valid(cols):
            raise ValueError(
                'cols must be an even integer between 4 and 16')
        self._cols = cols
        
        self._board = [] 
        for i in range(rows):
            self._board.append([])
            for j in range(cols):
                self._board[-1].append(NONE)


## Return values of private attributes
    def game_is_over(self):
        return self._gameover
                
    def get_turn(self):
        return self._turn

    
    def get_board(self):
        return self._board


    def get_winner(self):
        return self._winner


    def disc_in_cell(self,row,col): 
        return self._board[row][col]


## Basic methods for user
    def add_disc(self, row: int, col: int, color: int):
        '''Adds a disc at the specified position'''
        self._board[row][col] = color
        
    def remove_disc(self, row: int, col: int):
        '''Removes a disc at the specified position'''
        self._board[row][col] = NONE
        
    def switch_turn(self):
        '''Switches the attribute ._turn to the opposite value'''
        if self._turn == WHITE:
            self._turn = BLACK
        elif self._turn == BLACK:
            self._turn = WHITE


    def count_all_discs(self,color):
        '''Returns the number of discs on the board of a certain color'''
        count = 0
        for row in self._board:
            for entry in row:
                if entry == color:
                    count += 1
        return count


    def exists_valid_move(self,turn)->bool:
        '''For all cells on the board, checks if a valid move exists'''
        for row_num in range(self._rows):
            for col_num in range(self._cols):
                if self.disc_in_cell(row_num,col_num) == NONE:
                    try:
                        self._is_valid_move(row_num,col_num,turn)
                    except GameOverError:
                        return False
                    except InvalidMoveError:
                        pass
                    else:
                        return True
        return False

    
    def make_move(self,row,col):
        '''Makes a move on the Othello GameState'''
        self._is_valid_move(row,col,self._turn)
        list_of_moves = self._discs_to_flip(row,col,self._turn)
        
        self._board[row][col] = self._turn
        for move in list_of_moves:
            row,col = move
            self._board[row][col] = self._turn
            
        self.switch_turn()


    def determine_winner(self):
        '''Returns the winner of the game and stores it in the attribute
        self._winner'''
        self._gameover = True
        
        black_discs = self.count_all_discs(BLACK)
        white_discs = self.count_all_discs(WHITE)
        black_minus_white = black_discs - white_discs
        
        if black_minus_white == 0:
            self._winner = NONE
    
        elif self._win_rule == '>':
            if black_minus_white > 0:
                self._winner = BLACK
            else:
                self._winner = WHITE
                
        elif self._win_rule == '<':
            if black_minus_white < 0:
                self._winner = BLACK
            else:
                self._winner = WHITE
                
        return self._winner


## Private methods
    def _is_valid_move(self,row,col,turn):
        '''Checks if a move can be made or not'''
        self._require_game_not_over()
        self._require_valid_row_number(row)
        self._require_valid_column_number(col)
        self._require_empty_cell(row,col)
        if self._discs_to_flip(row,col,turn) == []:
            raise InvalidMoveError()

        
    def _discs_to_flip(self,row,col,turn):
        '''Returns a list of discs to be flipped in all directions'''
        list_of_discs = []

        list_of_discs.append(self._get_west_bound(row,col,turn)) 
        list_of_discs.append(self._get_east_bound(row,col,turn))
        list_of_discs.append(self._get_north_bound(row,col,turn))
        list_of_discs.append(self._get_south_bound(row,col,turn))
        list_of_discs.append(self._get_neast_bound(row,col,turn))
        list_of_discs.append(self._get_seast_bound(row,col,turn))
        list_of_discs.append(self._get_nwest_bound(row,col,turn))
        list_of_discs.append(self._get_swest_bound(row,col,turn))

        #Get rid of empty lists (moves in invalid directions)
        updated_list = []
        for sublist in list_of_discs:
            if sublist != []:
                for entry in sublist:
                    updated_list.append(entry)
        
        return updated_list

        
    def _get_west_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs west of the move that can be
        flipped.'''
        #Not a valid move if move is in first two cols
        invalid_move = []
        move_list = []
        if col < 2:
            return invalid_move
        #Not a valid move if adjacent disc is same color
        if self._board[row][col-1] == turn: 
            return invalid_move
        
        for col_num in range(col-1,-1,-1):
            #Not a valid move if adjacent cell is empty
            if self._board[row][col_num] == NONE:
                return invalid_move
            #Adjacent disc is other player's
            elif self._board[row][col_num] == opposite_turn(turn):
                move_list.append((row,col_num))
            #Adjacent disc is other player's and capped by own disc
            else:
                return move_list

        return invalid_move

    def _get_east_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs east of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if self._cols-col < 3:
            return invalid_move
        if self._board[row][col+1] == turn:
            return invalid_move

        for col_num in range(col+1,self._cols):
            if self._board[row][col_num] == NONE:
                return invalid_move
            elif self._board[row][col_num] == opposite_turn(turn):
                move_list.append((row,col_num))
            else:
                return move_list
            
        return invalid_move

    def _get_north_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs north of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if row < 2:
            return invalid_move
        if self._board[row-1][col] == turn:
            return invalid_move

        for row_num in range(row-1,-1,-1):
            if self._board[row_num][col] == NONE:
                return invalid_move              
            elif self._board[row_num][col] == opposite_turn(turn):
                move_list.append((row_num,col))
            else:
                return move_list

        return invalid_move

    def _get_south_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs south of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if self._rows-row < 3:
            return invalid_move
        if self._board[row+1][col] == turn:
            return invalid_move

        for row_num in range(row+1,self._rows):
            if self._board[row_num][col] == NONE:
                return invalid_move
            elif self._board[row_num][col] == opposite_turn(turn):
                move_list.append((row_num,col))
            else:
                return move_list
            
        return invalid_move

    def _get_neast_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs northeast of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if row < 2 or self._cols-col < 3:
            return invalid_move
        if self._board[row-1][col+1] == turn:
            return invalid_move

        current_row = row-1
        current_col = col+1
        while current_row > -1 and current_col < self._cols:

            if self._board[current_row][current_col] == NONE:
                return invalid_move
            elif self._board[current_row][current_col] == opposite_turn(turn):
                move_list.append((current_row,current_col))
            else:
                return move_list
            
            current_row -= 1
            current_col += 1

        return invalid_move
            
    def _get_nwest_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs northwest of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if row < 2 or col < 2: 
            return invalid_move
        if self._board[row-1][col-1] == turn:
            return invalid_move

        current_row = row-1
        current_col = col-1
        while current_row > -1 and current_col > -1:

            if self._board[current_row][current_col] == NONE:
                return invalid_move
            elif self._board[current_row][current_col] == opposite_turn(turn):
                move_list.append((current_row,current_col))
            else:
                return move_list
            
            current_row -= 1
            current_col -= 1

        return invalid_move

    def _get_swest_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs southwest of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if self._rows-row < 3 or col < 2: 
            return invalid_move
        if self._board[row+1][col-1] == turn:
            return invalid_move

        current_row = row+1
        current_col = col-1
        while current_row < self._rows and current_col > -1:

            if self._board[current_row][current_col] == NONE:
                return invalid_move
            elif self._board[current_row][current_col] == opposite_turn(turn):
                move_list.append((current_row,current_col))
            else:
                return move_list
            
            current_row += 1
            current_col -= 1

        return invalid_move

    def _get_seast_bound(self,row,col,turn)->'[moves]':
        '''Returns a list of the discs southeast of the move that can be
        flipped'''
        invalid_move = []
        move_list = []
        
        if self._rows-row < 3 or self._cols-col < 3: 
            return invalid_move
        if self._board[row+1][col+1] == turn:
            return invalid_move

        current_row = row+1
        current_col = col+1
        while current_row < self._rows and current_col < self._cols:

            if self._board[current_row][current_col] == NONE:
                return invalid_move
            elif self._board[current_row][current_col] == opposite_turn(turn):
                move_list.append((current_row,current_col))
            else:
                return move_list
            
            current_row += 1
            current_col += 1

        return invalid_move

## Error checking
    def _require_game_not_over(self):
        '''Raises GameOverError if there is a winner'''
        if self._gameover == True:
            raise GameOverError()

    
    def _require_empty_cell(self,row,col):
        '''Raises InvalidMoveError if the cell is not empty'''
        if self._board[row][col] != NONE:

            raise InvalidMoveError(
                'cannot place disc in a populated cell')

        
    def _require_valid_column_number(self,column_number):
        '''Raises an exception if column number is not a valid integer'''
        if type(column_number) != int or\
           not self._is_valid_column_number(column_number):

            raise ValueError(
                'column_number must be int between 0 and {}'.format(
                self._cols - 1))

        
    def _require_valid_row_number(self,row_number):
        '''Raises an exception if row number is not a valid integer'''
        if type(row_number) != int or\
           not self._is_valid_row_number(row_number):

            raise ValueError(
                'row_number must be int between 0 and {}'.format(
                self._rows - 1))                


    def _is_valid_column_number(self,column_number)->bool:
        '''Returns True if the given column number is valid;
        returns False otherwise'''
        return 0 <= column_number < self._cols


    def _is_valid_row_number(self,row_number)->bool:
        '''Returns True if the given row number is valid;
        returns False otherwise'''
        return 0 <= row_number < self._rows


## Utility functions
def _number_is_valid(number)->bool:
    '''Checks whether number is an even integer between 4 and 16'''
    if type(number) != int:
        return False
    elif number % 2 != 0:
        return False
    elif not (4 <= number <= 16):
        return False
    return True

def opposite_turn(turn:int)->int:
    '''Given a turn white or black, returns the opposite turn'''
    if turn == WHITE:
        return BLACK
    else:
        return WHITE

