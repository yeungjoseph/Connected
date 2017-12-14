#ifndef TICTACTOEAI_H
#define TICTACTOEAI_H

#include "tictactoe.h"

using namespace std;

class TicTacToeAI : public TicTacToe
{
    public:
    
    /**
     Creates a TicTacToe game with a computer player.
    */
    TicTacToeAI();
    
    /**
     The computer makes a move, ensuring that the player cannot win.
    */
    void computer_move();

    
    private:
    
     /**
     Checks for an empty spot that could lead to a win for the given player. If
     none are found, then it will check for an empty spot that will block the opponent
     from winning.
     @return The integer position of the spot if one exists, or -1 if none found.
    */
    int one_turn_from_win();
    
    /**
     Checks a single row for a winning sequence.
     @param best_row An integer that holds the current best spot to move.
     @param best_col An integer that holds the current best spot to move.
     @return The spot of the winning sequence for the computer or -1 if none found.
    */
    int check_row_win(int& best_row, int& best_col) const;
    
    /**
     Checks a single column for a winning sequence.
     @param best_row An integer that holds the current best spot to move.
     @param best_col An integer that holds the current best spot to move.
     @return The spot of the winning sequence for the computer or -1 if none found.
    */
    int check_col_win(int& best_row, int& best_col) const;
    
    /**
     Checks both diagonals for a winning sequence.
     @param best_row An integer that holds the current best spot to move.
     @param best_col An integer that holds the current best spot to move.
     @return The spot of the winning sequence for the computer or -1 if none found.
    */
    int check_diag_win(int& best_row, int& best_col) const;
    
    /**
     Checks a single line for a winning sequence given 3 cells in a tictactoe board.
     @param ar First cell row # to be checked.
     @param ac First cell col # to be checked.
     @param br Second cell row # to be checked.
     @param bc Second cell col # to be checked.
     @param cr Third cell row # to be checked.
     @param cc Third cell col # to be checked.
     @param best_row An integer that holds the current best spot to move.
     @param best_col An integer that holds the current best spot to move.
     @return The spot of the winning sequence for the computer or -1 if none found.
    */
    int check_line_win(int ar, int ac, int br, int bc, int cr, int cc, int& best_row, int& best_col) const;
    
    /**
     Makes the best possible move if neither player has a winning move the next turn.
    */
    void make_best_move();
    
    /**
     Finds the number of ways a player can win at a given unclaimed spot
     @param row The row number of the spot.
     @param col The column number of the spot.
     @return The number of ways the player can win.
    */
    int find_possible_wins(int row, int col) const;
};

#endif