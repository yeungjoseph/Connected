#Joseph Yeung 12752133
import Othello
import tkinter
import point

_BUTTON_FONT = ('Helvetica', 16)
_display = {0:'None',1:'White',2:'Black'}

class Game_Title:
    '''Shows the title bar for the game Othello. Displays the text
    'Othello-FULL' on the top of each window'''
    def __init__(self, root_window):

        self._game_title = tkinter.Label(master=root_window,
                            text='Othello - FULL', font=('Helvetica',48),
                            background = '#53CC2B')
    def _show(self):
             self._game_title.grid(row = 0, column = 0, columnspan = 2,
                              padx = 10, pady = 10,
                        sticky = tkinter.N  + tkinter.S + tkinter.E + tkinter.W)


class BoardDimensionDialog:
    '''Creates a dialog box with a scale for determining the initial dimensions
    of the Othello gameboard. By default, the dimensions are 8x8 cells'''
    def __init__(self, existing_rows, existing_cols):

        self._bdwindow = tkinter.Toplevel()
        self._existing_rows = existing_rows
        self._existing_cols = existing_cols
        self._rows = tkinter.IntVar()
        self._cols = tkinter.IntVar()
        self._ok_clicked = False

        dim_label = tkinter.Label(master = self._bdwindow,
                                  font = ('Helvetica',14),
            text = 'Choose the dimensions of the Othello gameboard')
        dim_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
                       sticky = tkinter.W)

        row_label = tkinter.Label(master = self._bdwindow,
                                  font = ('Helvetica',12),
                    text = 'Rows:')
        row_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tkinter.W)

        row_scale = tkinter.Scale(self._bdwindow, from_ = 4, to = 16,
                                  orient = tkinter.HORIZONTAL,
                                  variable = self._rows, resolution = 2)
        row_scale.grid(row = 2, column = 0, padx = 15, pady = 10, sticky = tkinter.W)

        col_label = tkinter.Label(master = self._bdwindow, font = ('Helvetica',12),
                    text = 'Cols:')
        col_label.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = tkinter.W)
        col_scale = tkinter.Scale(self._bdwindow, from_ = 4, to = 16,
                                  orient = tkinter.HORIZONTAL,
                                  variable = self._cols, resolution = 2)
        col_scale.grid(row = 2, column = 1, padx = 15, pady = 10, sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._bdwindow)
        button_frame.grid(row = 3, column = 1, padx = 5, pady = 5,
                          sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = ('Helvetica',12),
            command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5,
                       sticky = tkinter.E + tkinter.S)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = ('Helvetica',12),
            command =self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5,
                           sticky = tkinter.E + tkinter.S)

        self._bdwindow.rowconfigure(3, weight = 1)
        self._bdwindow.columnconfigure(1, weight = 1)

        row_scale.set(existing_rows)
        col_scale.set(existing_cols)

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._bdwindow.destroy()

    def _on_cancel_button(self) -> None:
        self._bdwindow.destroy()
        
    def show(self) -> None:
        self._bdwindow.grab_set()
        self._bdwindow.wait_window()

    def get_rows(self) -> int:
        if self._ok_clicked:
            return self._rows.get()
        return self._existing_rows

    def get_cols(self) -> int:
        if self._ok_clicked:
            return self._cols.get()
        return self._existing_cols

class WinRuleDialog:
    '''Creates a dialog box for determining the win rules of Othello. By default,
    the player with more pieces wins the game'''
    def __init__(self, existing_win_rule):

        self._existing_win_rule = existing_win_rule
        self._ok_button_clicked = False
        self._winrule_window = tkinter.Toplevel()
        self._win_rule = tkinter.StringVar()

        win_label = tkinter.Label(
            master = self._winrule_window, text = 'Pick the rules for Othello.',
            font = ('Helvectica',14))
        win_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        greater_wins_button = tkinter.Radiobutton(master = self._winrule_window,
                                      text= 'More discs win',
                                      variable = self._win_rule,
                                      value = '>') 
        greater_wins_button.grid(row = 1, column = 0, sticky = tkinter.W)
        
        less_wins_button =  tkinter.Radiobutton(master = self._winrule_window,
                                      text= 'Less discs win',
                                      variable = self._win_rule,
                                      value = '<')
        less_wins_button.grid(row = 2, column = 0, sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._winrule_window)
        button_frame.grid(row = 3, column = 0, padx = 5, pady = 5,
                          sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = ('Helvetica',12),
            command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5,
                       sticky = tkinter.E + tkinter.S)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = ('Helvetica',12),
            command =self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5,
                           sticky = tkinter.E + tkinter.S)

        self._winrule_window.rowconfigure(3, weight = 1)
        self._winrule_window.columnconfigure(0, weight = 1)

        if existing_win_rule == '>':       
            greater_wins_button.select()
        else:
            less_wins_button.select()

    def _on_ok_button(self) -> None:
        self._ok_button_clicked = True
        self._winrule_window.destroy()

    def _on_cancel_button(self) -> None:
        self._winrule_window.destroy()

    def show(self) -> None:
        self._winrule_window.grab_set()
        self._winrule_window.wait_window()

    def get_win_rule(self):
        if self._ok_button_clicked:
            return self._win_rule.get()
        return self._existing_win_rule


class FirstMoveDialog:
    '''Creates a dialog box for determining which player gets the first move.
    By default, the black starts the game'''
    def __init__(self, existing_first_move):

        self._existing_first_move = existing_first_move
        self._ok_button_clicked = False        
        self._firstmove_window = tkinter.Toplevel()
        self._first_move = tkinter.StringVar()

        win_label = tkinter.Label(
            master = self._firstmove_window,
            text = 'Pick the player who moves first.',
            font = ('Helvectica',14))
        win_label.grid(row = 0, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.W)

        black_moves_button = tkinter.Radiobutton(master = self._firstmove_window,
                                      text= 'Black',
                                      variable = self._first_move,
                                      value = 'B') 
        black_moves_button.grid(row = 1, column = 0, sticky = tkinter.W)
        
        white_moves_button =  tkinter.Radiobutton(master = self._firstmove_window,
                                      text= 'White',
                                      variable = self._first_move,
                                      value = 'W')
        white_moves_button.grid(row = 2, column = 0, sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._firstmove_window)
        button_frame.grid(row = 3, column = 0, padx = 5, pady = 5,
                          sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = ('Helvetica',12),
            command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5,
                       sticky = tkinter.E + tkinter.S)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = ('Helvetica',12),
            command =self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5,
                           sticky = tkinter.E + tkinter.S)

        self._firstmove_window.rowconfigure(3, weight = 1)
        self._firstmove_window.columnconfigure(0, weight = 1)

        if existing_first_move == 'B':
            black_moves_button.select()
        else:
            white_moves_button.select()

    def _on_ok_button(self) -> None:
        self._ok_button_clicked = True
        self._firstmove_window.destroy()

    def _on_cancel_button(self) -> None:
        self._firstmove_window.destroy()

    def show(self) -> None:
        self._firstmove_window.grab_set()
        self._firstmove_window.wait_window()

    def get_first_move(self):
        if self._ok_button_clicked:
            return self._first_move.get()
        return self._existing_first_move

      

class OthelloApplication:
    def __init__(self):

        self._root_window = tkinter.Tk()
        self._init_placing_started = False
        self._game_started = False

#Default Othello game settings
        self._win_rule = '>'
        self._first_move = 'B'
        self._rows = 8
        self._cols = 8
        self._gamestate = None

#Create and display top title bar of Othello
        Game_Title(self._root_window)._show()

#Create and configure a resizable canvas that will represent Othello game board
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#53CC2B')
        self._canvas.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N  + tkinter.S + tkinter.E + tkinter.W)

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

#Create and display sidebar for configuring the initial gamestate
        self._button_frame = tkinter.Frame(
            master = self._root_window, background = '#999999')
        self._button_frame.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        
        self._set_init_buttons()               
        

#Sidebar configurations
    def _set_init_buttons(self) -> None:
        '''Displays the buttons in the sidebar for setting up the initial
        configuration of the Othello game.'''
        
        setting_label = tkinter.Label(master=self._button_frame, text='Settings',
                           font= ('Helvetica', 16), background = '#BBBBBB')
        setting_label.grid(row = 0, column = 0, padx = 0, pady = 0,
                        sticky = tkinter.E + tkinter.W)

        dimensions_button = tkinter.Button(master = self._button_frame,
                                         text = 'Gameboard Dimensions',
                                         font = _BUTTON_FONT,
                                           command = self._configure_board_dimensions)
        dimensions_button.grid(row = 1, column = 0, padx = 5, pady = 5)

        first_move_button = tkinter.Button(master = self._button_frame,
                                           text = 'First Move',
                                           font = _BUTTON_FONT,
                                           command = self._configure_first_move)
        first_move_button.grid(row = 2, column = 0, padx = 5, pady = 5,
                     sticky = tkinter.E + tkinter.W)

        win_rule_button = tkinter.Button(master = self._button_frame,
                                         text = 'Win Rule',
                                         font = _BUTTON_FONT,
                                         command = self._configure_win_rule)
        win_rule_button.grid(row = 3, column = 0, padx = 5, pady = 5,
                     sticky = tkinter.E + tkinter.W)

        start_button = tkinter.Button(master = self._button_frame,
                                      text = 'START',
                                      font = _BUTTON_FONT,
                                      command = self._on_start)
        start_button.grid(row = 4, column = 0, padx = 5, pady = 150,
                     sticky = tkinter.E + tkinter.W + tkinter.S)

    def _set_placement_buttons(self) -> None:
        '''Displays the buttons in the sidebar for when the player is
        setting up the initial arrangement of discs on the gameboard'''

        self._placing_disc = tkinter.StringVar()
        
        place_black_button = tkinter.Radiobutton(master = self._button_frame,
                                text = 'Black', variable = self._placing_disc,
                                value = 'Black', font = _BUTTON_FONT,
                                command = self._display_placement_label)
        place_black_button.grid(row = 1, column = 0, padx = 5, pady = 10,
                                sticky = tkinter.W)
        place_black_button.select()
        
        place_white_button = tkinter.Radiobutton(master = self._button_frame,
                                text = 'White', variable = self._placing_disc,
                                value = 'White', font = _BUTTON_FONT,
                                command = self._display_placement_label)
        place_white_button.grid(row = 2, column = 0, padx = 5, pady = 10,
                                sticky = tkinter.W)

        play_button = tkinter.Button(master = self._button_frame,
                                     text = 'PLAY', font = _BUTTON_FONT,
                                     command = self._on_play)
        play_button.grid(row = 3, column = 0, padx = 5, pady = 50,
                         sticky = tkinter.W)
        
        self._display_placement_label()

        
    def _display_placement_label(self) -> None:
        '''Helper method for _set_placement_buttons to display the labels'''
        placement_label = tkinter.Label(master=self._button_frame,
                        text = 'Click an empty cell to\nadd a disc\n\n\
Click a popuplated cell\nto remove a disc',
                        font = ('Helvetica', 14), background = '#999999')
        placement_label.grid(row = 0, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.N + tkinter.W)

    def _set_play_labels(self) -> None:
        '''Sets the sidebar for when the game begins'''        
        self._turn_label = tkinter.Label(master=self._button_frame,
                        text = "{}'s turn.".format(
                            _display[self._gamestate.get_turn()]),
                        font = ('Helvetica', 14), background = '#999999')
        self._turn_label.grid(row = 0, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.N)

        black_label = tkinter.Label(master=self._button_frame,
                        text = 'Black: {}'.format(
                            self._gamestate.count_all_discs(Othello.BLACK)),
                        font = ('Helvetica', 14), background = '#999999')
        black_label.grid(row = 1, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.W)

        white_label = tkinter.Label(master=self._button_frame,
                        text = 'White: {}'.format(
                            self._gamestate.count_all_discs(Othello.WHITE)),
                        font = ('Helvetica', 14), background = '#999999')
        white_label.grid(row = 2, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.W)

    def _set_win_labels(self) -> None:
        '''Sets the sidebar for when the game is finished'''
        winner_label = tkinter.Label(master=self._button_frame,
                        text = 'Winner: {}'.format(
                            _display[self._gamestate.get_winner()]),
                        font = ('Helvetica', 14), background = '#999999')
        winner_label.grid(row = 0, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.N)
        
        black_label = tkinter.Label(master=self._button_frame,
                        text = 'Black: {}'.format(
                            self._gamestate.count_all_discs(Othello.BLACK)),
                        font = ('Helvetica', 14), background = '#999999')
        black_label.grid(row = 1, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.W)

        white_label = tkinter.Label(master=self._button_frame,
                        text = 'White: {}'.format(
                            self._gamestate.count_all_discs(Othello.WHITE)),
                        font = ('Helvetica', 14), background = '#999999')
        white_label.grid(row = 2, column = 0, padx = 5, pady = 15,
                             sticky = tkinter.W)

        play_again_button = tkinter.Button(master=self._button_frame,
                        text = 'PLAY AGAIN!', font = _BUTTON_FONT,
                        command = self._on_play_again)
        play_again_button.grid(row = 3, column = 0, padx = 5, pady = 15,
                               sticky = tkinter.E)
                                           

        quit_button = tkinter.Button(master=self._button_frame, text = 'QUIT',
                                    font = ('Helvetica', 12),
                                    command = self._on_exit)
        quit_button.grid(row = 4, column = 0, padx = 5, pady = 30,
                         sticky = tkinter.S + tkinter.E)

    def _on_exit(self) -> None:
        '''When the player clicks 'EXIT' button, the program ends'''
        self._root_window.destroy()

    def _on_play_again(self) -> None:
        '''When the player clicks 'PLAY AGAIN!' button, another game starts'''
        self._root_window.destroy()
        OthelloApplication().run()        
    
    def _configure_board_dimensions(self) -> None:
        '''Initiates a pop-up window to prompt the user for configuring the
        initial board dimensions'''
        board_dimensions = BoardDimensionDialog(self._rows, self._cols)
        board_dimensions.show()

        self._rows = board_dimensions.get_rows()
        self._cols = board_dimensions.get_cols()


    def _configure_win_rule(self) -> None:
        '''Whenever user clicks the win rule button, a WinRuleDialog pops up'''
        win_rule_dialog = WinRuleDialog(self._win_rule)
        win_rule_dialog.show()

        self._win_rule = win_rule_dialog.get_win_rule()


    def _configure_first_move(self) -> None:
        '''Whenever user clicks the first move button, a FirstMoveDialog pops up'''
        first_move_dialog = FirstMoveDialog(self._first_move)
        first_move_dialog.show()

        self._first_move = first_move_dialog.get_first_move()


    def _on_start(self) -> None:
        '''Once the user clicks 'START' a new game is created and initial
        placement of discs begins'''
        self._gamestate = Othello.GameState(self._first_move, self._win_rule,
                                            self._rows,self._cols)
        self._init_placing_started = True

        self._draw_board()
        self._clear_side_frame()
        self._set_placement_buttons()


    def _on_play(self) -> None:
        '''Once the user clicks 'PLAY' the game begins and players take turns
        placing discs until the game ends'''
        self._game_started = True
        self._clear_side_frame()

        if self._gamestate.exists_valid_move(self._gamestate.get_turn()):
            pass

        elif self._gamestate.exists_valid_move(Othello.opposite_turn(
               self._gamestate.get_turn())):
            self._gamestate.switch_turn()

        else:
            self._gamestate.determine_winner()
            self._set_win_labels()
            return

        self._set_play_labels()


    def _clear_side_frame(self) -> None:
        '''Clears the sideframe of all widgets'''
        for widget in self._button_frame.winfo_children():
            widget.destroy()


##Canvas configurations    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Redraw the gameboard whenever the canvas is resized'''
        if self._gamestate != None:
            self._draw_board()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''Whenever the canvas is clicked, handle the click'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_point = point.from_pixel(
            event.x, event.y, width, height)

        row = self._point_in_row(click_point)
        col = self._point_in_col(click_point)

        convert_to_int = {'Black':Othello.BLACK,'White':Othello.WHITE}
        
        if self._gamestate == None or self._gamestate.game_is_over():
            return
        
        if self._init_placing_started == True and self._game_started == False:
            if self._gamestate.disc_in_cell(row,col) == Othello.NONE:
                self._gamestate.add_disc(row,col,
                        convert_to_int[self._placing_disc.get()])
            else:
                self._gamestate.remove_disc(row,col)

            self._draw_board()

        elif self._init_placing_started == True and self._game_started == True:
            if self._gamestate.exists_valid_move(self._gamestate.get_turn()):
                try:
                    self._gamestate.make_move(row,col)
                    self._draw_board()
                except (Othello.InvalidMoveError,ValueError):
                    pass
                    
            if self._gamestate.exists_valid_move(Othello.opposite_turn(
               self._gamestate.get_turn())) and not\
               self._gamestate.exists_valid_move(self._gamestate.get_turn()):
                self._gamestate.switch_turn()

            elif not self._gamestate.exists_valid_move(self._gamestate.get_turn()) and\
               not self._gamestate.exists_valid_move(Othello.opposite_turn(
               self._gamestate.get_turn())):
                
                self._gamestate.determine_winner()
                self._set_win_labels()
                return

            self._set_play_labels()
            

        
    def _draw_board(self) -> None:
        '''Draw the gameboard depending on which cells are populated in the
        gameboard'''
        self._canvas.delete(tkinter.ALL)
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        for rows in range(1,self._gamestate._rows):
            self._canvas.create_line(0,height/self._gamestate._rows*rows,
                                     width,height/self._gamestate._rows*rows,
                                     fill = 'black')
            
        for cols in range(1,self._gamestate._cols):
            self._canvas.create_line(width/self._gamestate._cols*cols,0,
                                     width/self._gamestate._cols*cols,height,
                                     fill = 'black')
        self._draw_all_discs()
        

    def _draw_all_discs(self) -> None:
        '''Draws all the discs onto the canvas'''   
        for row in range(self._gamestate._rows):
            for col in range(self._gamestate._cols):
                color = self._gamestate.disc_in_cell(row,col)
                if color != Othello.NONE:
                    self._draw_disc(row,col,color)

                    
    def _draw_disc(self,row:int,col:int,color:int) -> None:
        '''Draws a single disc onto the canvas given a row, column, and color'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        row_interval = height/self._rows
        col_interval = width/self._cols

        if color == Othello.BLACK:
            hex_color = '#000000'
        else:
            hex_color = '#FFFFFF'
        
        self._canvas.create_oval(
            0+col*col_interval+3,0+row*row_interval+3,
            0+col*col_interval+col_interval-3,
            0+row*row_interval+row_interval-3,
            fill=hex_color)

    def _point_in_row(self, point1: point.Point):
        '''Returns the row that the point resides in'''
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width()
        point_y = point1.pixel(width,height)[1]
        interval = height/self._rows

        first_row_bound = 0
        for row in range(self._rows):
            if 0 < point_y < first_row_bound+interval:
                return row
            first_row_bound += interval
            
    def _point_in_col(self, point1: point.Point):
        '''Returns the column that the point resides in'''
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width()
        point_x = point1.pixel(width,height)[0]
        interval = width/self._cols

        first_col_bound = 0
        for col in range(self._cols):
            if 0 < point_x < first_col_bound+interval:
                return col
            first_col_bound += interval
    
    
    def run(self) -> None:
        self._root_window.mainloop()

    
if __name__ == '__main__':
    OthelloApplication().run()
