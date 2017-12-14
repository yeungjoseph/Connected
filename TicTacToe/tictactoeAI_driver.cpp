#include <iostream>
#include <string>
#include "tictactoeAI.h"

using namespace std;

/**
 Play a game of TicTacToe in the console with the computer.
*/
int main()
{
    //Create game & print welcome message
    TicTacToeAI game = TicTacToeAI();
    cout << game.helpstring();
    
    //Prompt user for which player should move first
    string player;
    do
    {
        cout << "TicTacToe - Enter 1 to move first or 2 to move second." << endl;
        getline(cin, player);
        if (player.find("2") != string::npos)
        {
            game.set_current_turn(2);
            game.computer_move();
        }
    } while(player.find("1") == string::npos && player.find("2") == string::npos);
    
    //Player and computer takes turns making moves until game is over
    int move = 0;
    while (!game.check_gameover())
    {
        cout << "Current turn: Player " << game.get_current_turn() << endl;
        cout << game.tostring();
        try
        {
            cout << "Enter the spot to move (1-9): ";
            cin >> move;
            game.move(move);
            if (!game.check_gameover())
            {
                game.computer_move();
            }
        }
        catch (const exception&)
        {
            cout << "That is an invalid move. Please try again." << endl;
        }
    }
    
    //Prints the winning player and the resulting board
    int winner = game.find_winner();
    if (winner != 0)
    {
        cout << "Winner: Player " << winner << endl;
    }
    else
    {
        cout << "Tie game!" << endl;
    }
    cout << game.tostring();
    
    return 0;

}