#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <string>

using namespace std;

class TicTacToe
{
    public:
    
    /**
     Constructs a TicTacToe game.
    */
    TicTacToe();
    
    /**
     Sets the current turn of a player.
     @param player An integer representation of the player (1 or 2).
    */
    void set_current_turn(int player);
    
    /**
     Returns the player whose turn it is.
     @return an integer representing which player is about to move.
    */
    int get_current_turn() const;
    
    /**
     Processes the current player's move and attempts to update the gameboard.
     @param spot An integer 1-9 that specifies the spot to move.
    */
    void move(int spot); 
    
    /**
     Checks if there is a player who has 3 pieces in a row.
     @return An int corresponding to the winning player or 0 for none.
    */
    int find_winner() const; 
    
    /**
     Checks whether the game is over.
     @return true if the game is over else false.
    */
    bool check_gameover() const; 
    
    /**
     Creates a string representation of a TicTacToe board.
     @return A string representing the current state of the TicTacToe game.
    */
    string tostring() const;
    
    /**
     Prints a string representation of a TicTacToe board with its cells labeled.
     @return A string representing the TicTacToe board with numbered cells.
    */
    string helpstring() const;
    
    /**
     Resets the TicTacToe game to its initial state.
    */
    void new_game();
    
    
    protected:
    /**
     Returns the piece at a given spot 1-9 inclusive.
     @param spot An integer 1-9 that specifies the spot to query.
     @return An integer representing the player at the spot or 0 for none.
    */
    int piece_at(int spot) const;
    
    /**
     Helper method that converts a 2D array index to a corresponding spot 1-9
     @row The row of the 3x3 matrix to convert.
     @col The column of the 3x3 matrix to convert.
     @return The corresponding integer 1-9 inclusive that represents the given spot.
    */
    int indices_to_spot(int row, int col) const;
    
    /**
     Returns the number of turns.
     @return An integer representing the number of turns passed.
    */
    int get_num_turns() const;
    int gameboard [3][3];
    
    private:
    int current_turn; 
    int num_turns;
};

#endif