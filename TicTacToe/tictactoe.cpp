#include <string>
#include <sstream>
#include <exception>

#include "tictactoe.h"

using namespace std;


//Unnamed namespace to keep helper functions local in scope.
namespace
{
    /**
     * Helper function that initializes a 3x3 int matrix to all 0's.
     * @param a A 3x3 integer matrix.
    */
    void setArrayToZero(int a[3][3])
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                a[i][j] = 0;
            }
        }
    }
}


//This exception is thrown whenever the player tries making an invalid move.
class InvalidMove: public exception
{
    /**
     * Defines the error message to display when this exception is thrown.
     * @return the error message to be displayed.
    */
    virtual const char* what() const throw()
    {
        return "This spot is already taken or out of range.";
    }
};



/**
 * Constructs a TicTacToe game.
*/
TicTacToe::TicTacToe() :
    num_turns(0), current_turn(1)
{
    setArrayToZero(gameboard);
}

/**
 Sets the current turn of a player.
 @param player An integer representation of the player (1 or 2).
*/
void TicTacToe::set_current_turn(int player)
{
    if (player == 1 || player == 2)
    {
        current_turn = player;
    }
}

/**
 Returns the player whose turn it is.
 @return an integer representing which player is about to move.
*/
int TicTacToe::get_current_turn() const
{
    return current_turn;
}


/**
 * Creates a string representation of a TicTacToe board.
 * @return A string representing the current state of the TicTacToe game.
*/
string TicTacToe::tostring() const
{
    ostringstream board;
    for (int row = 0; row < 3; row++)
    {
        board << "+---+---+---+" << endl;
        for (int col = 0; col < 3; col++)
        {
            switch(gameboard[row][col])
            {
                case 0: board << "|   "; break;
                case 1: board << "| X "; break;
                case 2: board << "| O "; break;
            }
        }
        board << "|" << endl;
    }
    board << "+---+---+---+" << endl;
    
    return board.str();
}


/**
 * Processes the current player's move and attempts to update the gameboard.
 * @param spot An integer 1-9 that specifies the spot to move.
*/
void TicTacToe::move(int spot)
{
    
    //Check that spot is between 1-9.
    int row; int col;
    switch (spot)
    {
        case 1: row = 0; col = 0; break;
        case 2: row = 0; col = 1; break;
        case 3: row = 0; col = 2; break;
        case 4: row = 1; col = 0; break;
        case 5: row = 1; col = 1; break;
        case 6: row = 1; col = 2; break;
        case 7: row = 2; col = 0; break;
        case 8: row = 2; col = 1; break;
        case 9: row = 2; col = 2; break;
        default: throw InvalidMove();
    }
    
    //Check that the spot the player wants to move in is empty.
    if (gameboard[row][col] != 0)
        throw InvalidMove();
    
    //Update gameboard, current player, and num_turns
    gameboard[row][col] = current_turn;
    current_turn = (current_turn == 1) ? 2 : 1; 
    num_turns++;
}


/**
 * Checks if there is a player who has 3 pieces in a row.
 * @return An int corresponding to the winning player or 0 for none.
*/
int TicTacToe::find_winner() const
{
    for (int line = 0; line < 3; line++)
    {
        //Checks all rows for 3 in a row
        if (gameboard[line][0] != 0 && gameboard[line][0] == gameboard[line][1] 
            && gameboard[line][1] == gameboard[line][2])
            return gameboard[line][0];
            
        //Checks all columns for 3 in a row
        else if (gameboard[0][line] != 0 && gameboard[0][line] == gameboard[1][line]
            && gameboard[1][line] == gameboard[2][line])
            return gameboard[0][line];
    }
            
    //Checks both diagonals for 3 in a row
    if (gameboard[1][1] != 0 &&
        (gameboard[0][0] == gameboard[1][1] && gameboard[1][1] == gameboard[2][2]) ||
        (gameboard[0][2] == gameboard[1][1] && gameboard[1][1] == gameboard[2][0]))
        return gameboard[1][1];
    
    //No players have 3 in a row 
    return 0;     
}


/**
 * Checks whether the game is over.
 * @return true if the game is over else false.
*/
bool TicTacToe::check_gameover() const
{
    //Impossible for game to be over in first 4 rounds
    if (num_turns < 5)
    {
        return false;
    }
    //Game board is full and cannot take any more moves
    if (num_turns >= 9)
    {
        return true;
    }
    //Check for 3 in a row
    return (find_winner() == 0) ? false : true; 
}


/**
 * Resets the TicTacToe game to its initial state.
*/
void TicTacToe::new_game()
{
    setArrayToZero(gameboard);
    current_turn = 1;
    num_turns = 0;
}

/**
 Prints a string representation of a TicTacToe board with its cells labeled.
 @return A string representing the TicTacToe board with numbered cells.
*/
string TicTacToe::helpstring() const
{
    ostringstream numbered_board;
    
    numbered_board << "+---+---+---+" << endl;
    numbered_board << "| 1 | 2 | 3 |" << endl;   
    numbered_board << "+---+---+---+" << endl;
    numbered_board << "| 4 | 5 | 6 |" << endl;
    numbered_board << "+---+---+---+" << endl;
    numbered_board << "| 7 | 8 | 9 |" << endl;
    numbered_board << "+---+---+---+" << endl;
    
    return numbered_board.str();   
}

/**
 Returns the piece at a given spot 1-9 inclusive.
*/
int TicTacToe::piece_at(int spot) const
{
    int row; int col;
    switch (spot)
    {
        case 1: row = 0; col = 0; break;
        case 2: row = 0; col = 1; break;
        case 3: row = 0; col = 2; break;
        case 4: row = 1; col = 0; break;
        case 5: row = 1; col = 1; break;
        case 6: row = 1; col = 2; break;
        case 7: row = 2; col = 0; break;
        case 8: row = 2; col = 1; break;
        case 9: row = 2; col = 2; break;
        default: return -1;
    }
    return gameboard[row][col];
}

/**
 Helper method that converts a 2D array index to a corresponding spot 1-9
 @row The row of the 3x3 matrix to convert.
 @col The column of the 3x3 matrix to convert.
 @return The corresponding integer 1-9 inclusive that represents the given spot.
*/
int TicTacToe::indices_to_spot(int row, int col) const
{
    return row * 3 + col + 1;
}

/**
 Returns the number of turns.
 @return An integer representing the number of turns passed.
*/
int TicTacToe::get_num_turns() const
{
    return num_turns;
}