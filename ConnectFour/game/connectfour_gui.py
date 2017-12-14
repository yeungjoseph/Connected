import connectfour, tkinter, point
from PIL.ImageTk import PhotoImage

'''
To-do list:
1a. Add player labels #DONE
1b. Show current turn #DONE
2. Create animation for hovering/dropping #DONE
3. Add ability to change disc colors *problem finding way to change button image
4. Improve winner popup dialog #DONE
5. Deal with tie games
6. Timer between moves (option)
7. Music w/ mute button
8. Add option for pop
'''

class WinnerDialog:
    '''
    Creates a dialog box for when a winner is determined.
    '''
    def __init__(self, winner: int):
        win_dict = {connectfour.RED:'Player 1',
                    connectfour.YELLOW:'Player 2'}
        top = tkinter.Toplevel(bd = 10, relief = tkinter.SUNKEN,
                               bg = '#1a75ff')
        top.title('Winner!!!')
        
        win_label = tkinter.Label(master = top, bg = '#1a75ff', fg = 'white',
                                  text = 'Winner: {}!'.format(
                                      win_dict[winner]),
                                  font = ('Helvetica',14))
        ok_button = tkinter.Button(master = top, text = 'Ok', bg = '#1a75ff',
                                   font = ('Helvetica',12), fg = 'white',
                                   activebackground = '#6ba3ff',
                                   activeforeground = 'white',
                                   command = top.destroy)
        
        win_label.grid(row = 0, padx = 10, pady = 10)
        ok_button.grid(row = 1, padx = 10, pady = 10)
        
        
class ConnectFourApp:
    '''
    Defines a ConnectFour game and its associated methods.
    '''
    BOARD_ROWS = 6
    BOARD_COLS = 7
    label_dict = {connectfour.RED:'  Player 1\'s turn',
                    connectfour.YELLOW:'  Player 2\'s turn'}
    fill_dict = {connectfour.NONE:'#6ba3ff',connectfour.RED:'red',
                     connectfour.YELLOW:'black'}  
    
    def __init__(self):
        '''
        Initialize variables and GUI when the program first runs.
        '''
        self._game_started = False
        self._gamestate = connectfour.new_game()
        self._winner = connectfour.NONE
        self._playcount = 0
        
        #Initialize Tk objects
        self._root_window = tkinter.Tk()
        self._root_window.configure(background = '#6ba3ff')
        
        self._p1 = PhotoImage(file='redcircle.png')
        self._p2 = PhotoImage(file='blackcircle.png')
        
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 800, height = 500,
            background = '#6ba3ff', highlightthickness = 0)      
        name_label = tkinter.Label(master = self._root_window, 
                                   font = ('Helvetica', 60),
                                   text = 'Connect Four', bg = '#6ba3ff',
                                   fg = 'white')
        self.play_button = tkinter.Button(master = self._root_window,
                                     text = 'PLAY', font = ('Helvetica',35),
                                     command = self._on_play_button,
                                     bg = '#005ce6', fg = 'white',
                                     activeforeground = 'white',
                                     activebackground = '#80b3ff')
        p1_label = tkinter.Label(master = self._root_window,
                                   text = 'Player 1  ', font = ('Helvetica',30),
                                   image = self._p1, compound = tkinter.RIGHT,
                                   bg = '#1a75ff', fg = 'white', bd = 10)
        p2_label = tkinter.Label(master = self._root_window,
                                   text = 'Player 2  ', font = ('Helvetica',30),
                                   image = self._p2, compound = tkinter.RIGHT,
                                   bg = '#1a75ff', fg = 'white', bd = 10)
        
        #Place objects to desired locations
        self._canvas.grid(row = 2, sticky = tkinter.N  + tkinter.S + 
                          tkinter.E + tkinter.W, columnspan = 2)
        name_label.grid(row = 0, padx = 10, pady = 10, 
                        sticky = tkinter.N, columnspan = 2)
        p1_label.grid(row = 3, padx = 40, pady = 5, sticky = tkinter.W)
        p2_label.grid(row = 3, column = 1, padx = 40, pady = 5,
                      sticky = tkinter.E)
        self.play_button.grid(row = 4, pady = 15, padx = 80, columnspan = 2)

        
        #Configure resizing of windows
        self._root_window.minsize(width=700,height=450)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.rowconfigure(0, weight = 1)
        self._canvas.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
        self._canvas.bind('<Motion>', self._on_mouse_moved)
        self._canvas.bind('<ButtonRelease-1>', self._on_canvas_clicked)
        
        
    #Helper/local functions
    def _on_play_button(self) -> None:
        '''
        Changes the GUI once the play button is clicked.
        '''
        if self._game_started:
            self._root_window.destroy() 
        self._game_started = True
        
        if self._playcount == 0: #only create label once
            self.turn_label = tkinter.Label(master=self._root_window,
                text = ConnectFourApp.label_dict[self._gamestate[1]],
                font = ('Helvetica',30), background = '#6ba3ff',
                image = self._p1, compound = tkinter.LEFT)
            self.turn_label.grid(row = 1, columnspan = 2)
        
        if self._winner != connectfour.NONE:            
            self._new_game()
            
        self.play_button.configure(text = 'QUIT')
        
        
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_board()
        
        
    def _on_mouse_moved(self, event: tkinter.Event) -> None:
        '''
        Handles mouse movement and disc animation.
        '''
        if self._game_started:
            width = self._canvas.winfo_width()
            height = self._canvas.winfo_height()
            col = self._point_in_col(
                point.from_pixel(event.x, event.y, width, height))
            
            if col != None:
                #draw disc on top row depending on col and turn
                xmargin = 1/7
                ymargin = 1/18
                x_incr = (width - width*xmargin)/11 
                y_incr = (height - height*ymargin)/8
                
                top_left_x = (width*xmargin + x_incr/3) + (col-1)*(5/4)*x_incr
                bottom_right_x = top_left_x + x_incr 
                top_left_y = height*ymargin + y_incr/5
                bottom_right_y = top_left_y + y_incr
                
                self._draw_board()
                self._canvas.create_oval(top_left_x, top_left_y,
                    bottom_right_x, bottom_right_y,
                     fill = ConnectFourApp.fill_dict[self._gamestate[1]]) 
        
        
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''
        Handles disc dropping.
        '''
        if self._game_started:
            width = self._canvas.winfo_width()
            height = self._canvas.winfo_height()
            col = self._point_in_col(
                point.from_pixel(event.x, event.y, width, height))
       
        #Make move
            try:
                self._gamestate = connectfour.make_move(self._gamestate, col)
            except connectfour.InvalidMoveError:
                return 
            else:
                self._update_turn()
       
        #Draw board
            self._draw_board()
        
        #Check for winner
            self._winner = connectfour.winner(self._gamestate)
            if self._winner != connectfour.NONE:
                WinnerDialog(self._winner)
                self._game_started = False
                self.play_button.configure(text = 'PLAY AGAIN!')
                
                
    def _update_turn(self):
        '''
        Changes the turn of the current player.
        '''
        img_dict = {connectfour.RED : self._p1, connectfour.YELLOW : self._p2}
        self.turn_label.config(
            text = ConnectFourApp.label_dict[self._gamestate[1]])
        self.turn_label.config(image = img_dict[self._gamestate[1]])
    
    
    def _new_game(self):
        '''
        Creates a new connect four game.
        '''
        self._gamestate = connectfour.new_game()
        self._winner = connectfour.NONE
        self._update_turn()
        self._draw_board()
        self._playcount += 1
                   
        
    def _draw_board(self) -> None:
        '''
        Draws the connect four board along with all the discs.
        '''
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        self._canvas.create_rectangle(canvas_width/7, canvas_height/18,
                                      canvas_width-(canvas_width/7),
                                      canvas_height-(canvas_height/18),
                                      fill = 'yellow')
        self._draw_discs(canvas_width,canvas_height)
    
    
    def _draw_discs(self,width,height) -> None:
        '''
        Draws all discs on the board.
        '''
        xmargin = 1/7
        ymargin = 1/18
                
        x_incr = (width - width*xmargin)/11 #divisor modifier adjusts disc size
        y_incr = (height - height*ymargin)/8
        curr_x = width*xmargin + x_incr/3 #add a small margin around board
        curr_y = height*ymargin + y_incr/5
        
        for row in range(ConnectFourApp.BOARD_ROWS):
            for col in range(ConnectFourApp.BOARD_COLS): 
                self._canvas.create_oval(curr_x, curr_y, curr_x + x_incr,
                                         curr_y + y_incr,
                    fill = ConnectFourApp.fill_dict[self._gamestate.board[col][row]])
                curr_x += x_incr + x_incr/4 #adds a buffer between discs
            curr_x = width*xmargin + x_incr/3
            curr_y += y_incr + y_incr/5
            
            
    def _point_in_col(self, pt: point.Point):
        '''
        Checks which column a particular point resides in.
        '''
        x_coord = pt.frac()[0]
        x_board_size = 5/7 #fraction of canvas that makes up game board     
        interval = x_board_size/connectfour.BOARD_COLUMNS
        
        first_col_bound = 1/7
        for col in range(connectfour.BOARD_COLUMNS):
            if first_col_bound < x_coord < first_col_bound + interval:
                return col + 1
            first_col_bound += interval
                
        
        
    def run(self) -> None:
        self._root_window.mainloop()


if __name__ == '__main__':
    ConnectFourApp().run()
