i#include "tictactoeAI.h"

/**
 Creates a TicTacToe game with a computer player.
*/
TicTacToeAI::TicTacToeAI() : TicTacToe() {}

/**
 The computer makes a move, ensuring that the player cannot win.
*/
void TicTacToeAI::computer_move()
{
    //First move should be either middle or upper left corner
    if (get_num_turns() == 0 || get_num_turns() == 1)
    {
        if (piece_at(5) == 0)
        {
            TicTacToe::move(5);
        }
        else
        {
            TicTacToe::move(1);
        }
    }
    
    else
    {
        //Checks any one-move-from-winning scenarios
        int spot = one_turn_from_win();
        if (spot > 0)
        {
            TicTacToe::move(spot);
        }
        
        //Take any move that would maximize computer chances of winning
        else
        {
            make_best_move();
            
        }
    }
}

/**
 Checks for an empty spot that could lead to a win for the given player. If
 none are found, then it will check for an empty spot that will block the opponent
 from winning.
 @return The integer position of the spot if one exists, or -1 if none found.
*/
int TicTacToeAI::one_turn_from_win() 
{
    int best_row = -1; //Used to store a move that defends against a win
    int best_col = -1; //computer will take this move if it cannot win this turn
    int spot = -1;     //The spot the computer will move
    
    //Check rows, cols, and diagonals for any move that can win
    //also store any move that will block a potential win by the opponent
    spot = check_row_win(best_row, best_col);
    if (spot > 0)
    {
        return spot; //Found an offensive move!
    }
        
    spot = check_col_win(best_row, best_col);
    if (spot > 0)
    {
        return spot; //Found an offensive move!
    }
        
    spot = check_diag_win(best_row, best_col);
    if (spot > 0)
    {
        return spot; //Found an offensive move!
    }
    
    //Found a defensive move!
    if (best_row != -1 && best_col != -1)
    {
        return indices_to_spot(best_row, best_col);
    }
    
    return spot;
}

/**
 Checks a single row for a winning sequence.
 @param best_row An integer that holds the current best spot to move.
 @param best_col An integer that holds the current best spot to move.
 @return The spot of the winning sequence for the computer or -1 if none found.
*/
int TicTacToeAI::check_row_win(int& best_row, int& best_col) const
{
    int spot = -1;
    for (int row = 0; row < 3; row++)
    {
        spot = check_line_win(row,0,row,1,row,2, best_row, best_col);
        if (spot > 0)
        {
            return spot;
        }
    }
    return spot;
}

/**
 Checks a single column for a winning sequence.
 @param best_row An integer that holds the current best spot to move.
 @param best_col An integer that holds the current best spot to move.
 @return The spot of the winning sequence for the computer or -1 if none found.
*/
int TicTacToeAI::check_col_win(int& best_row, int& best_col) const
{
    int spot = -1;
    for (int col = 0; col < 3; col++)
    {
        spot = check_line_win(0,col,1,col,2,col, best_row, best_col);
        if (spot > 0)
        {
            return spot;
        }
    }
    return spot;
}

    
/**
 Checks both diagonals for a winning sequence.
 @param best_row An integer that holds the current best spot to move.
 @param best_col An integer that holds the current best spot to move.
 @return The spot of the winning sequence for the computer or -1 if none found.
*/
int TicTacToeAI::check_diag_win(int& best_row, int& best_col) const
{
    //Check first diag
    int spot = check_line_win(0,0,1,1,2,2, best_row, best_col);
    if (spot > 0)
    {
        return spot;
    }
   
    //Check second diag
    return check_line_win(0,2,1,1,2,0, best_row, best_col);
  
}

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
int TicTacToeAI::check_line_win(int ar, int ac, int br, int bc, int cr, int cc, 
                                int& best_row, int& best_col) const
{
    //Keep track of how many times each player shows up in a line
    int player_cnt = 0;
    int opp_cnt = 0;
    //Temp holds a possible spot to block the opposing player from winning
    int temp_row = -1;
    int temp_col = -1;
    int opp_player = (get_current_turn() == 1) ? 2 : 1;
    int cells[3][2] = {{ar,ac},{br,bc},{cr,cc}}; //The three cells to check
    
    for (int cell = 0; cell < 3; cell++)
    {
        if (gameboard[cells[cell][0]][cells[cell][1]] == get_current_turn())
        {
            player_cnt++;
        }
        else if (gameboard[cells[cell][0]][cells[cell][1]] == opp_player)
        {
            opp_cnt++;
        }
        else
        {
            temp_row = cells[cell][0];
            temp_col = cells[cell][1];
        }
    }
    
    //A winning move is found for the computer
    if (player_cnt == 2 && temp_row != -1 && temp_col != -1)
        {
            return indices_to_spot(temp_row, temp_col);
        }
    //The user is about to win
    else if (opp_cnt == 2 && temp_row != -1 && temp_col != -1) 
    {
        best_row = temp_row;
        best_col = temp_col;
    }
    return -1;
}

/**
 Makes the best possible move if neither player has a winning move the next turn.
*/
void TicTacToeAI::make_best_move()
{
    int temp_row = -1;
    int temp_col = -1;
    int max_possible_wins = -1;
    for(int row = 0; row < 3; row++)
    {
        for (int col = 0; col < 3; col++)
        {
            if (gameboard[row][col] == 0)
            {
                int possible_wins = find_possible_wins(row,col);
                if (possible_wins > max_possible_wins)
                {
                    temp_row = row;
                    temp_col = col;
                }
            }
        }
    }
    TicTacToe::move(indices_to_spot(temp_row,temp_col));
}

/**
 Finds the number of ways a player can win at a given unclaimed spot
 @param row The row number of the spot.
 @param col The column number of the spot.
 @return The number of ways the player can win.
*/
int TicTacToeAI::find_possible_wins(int row, int col) const
{
    int possible_wins = 0;
    int opp_player = (get_current_turn() == 1) ? 2 : 1;
    
    if (gameboard[row][0] != opp_player && gameboard[row][1] != opp_player
    && gameboard[row][2] != opp_player)
    {
        possible_wins++;
    }
    
    if (gameboard[0][col] != opp_player && gameboard[1][col] != opp_player
    && gameboard[2][col] != opp_player)
    {
        possible_wins++;
    }
    
    //If the middle is the opponent's piece, no need to check for diagonals
    if (gameboard[1][1] == opp_player)
    {
        return possible_wins;
    }
    
    //Diagonal going from top left to bottom right
    if (row == col)
    {
        if (gameboard[0][0] != opp_player && gameboard[2][2] != opp_player)
        {
            possible_wins++;
        }
    }
    //Diagonal going from top right to bottom left
    else if ((col == 0 || col == 2) && (row == 0 || row == 2))
    {
        if (gameboard[0][2] != opp_player && gameboard[2][0] != opp_player)
        {
            possible_wins++;
        }
    }
    
    return possible_wins;
}