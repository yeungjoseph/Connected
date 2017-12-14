About This Program
--

Like Othello, TicTacToe is entirely a course project. The instructions were to
create a program that allows a player to play Tic Tac Toe against a computer that
will never lose. I included this program on my GitHub because it reveals a greater
understanding of object-oriented design and how classes and inheritance can help
achieve clearer code, even though an object-oriented paradigm was not required, or even
suggested for this project. 

My biggest success in this project was being able to modularize a specific function in tictactoeAI.cpp 
(check_line_win:line 158). I encountered a similar problem while traversing a 2d array in Othello 
last year, and ended up writing 8 functions with very similar code to check every direction 
(north, northeast, east, etc...) of a 2d array. This time, I was able to write one function that could 
be reused to create much simpler functions when checking columns, rows, and diagonals. One problem I 
would like to fix in the function check_line_win is to switch out the ugly mess of integer parameters
for a clearer Point struct. The reason I did not do so in my original project was because that structs 
were not introduced in our course and I wanted to get a working prototype as soon as possible using the
tools I was most confident in. Trying to solve the problem while learning a new tool introduces two
points of failure while coding: misuse of the tool and faulty programming logic. It was a much better
idea to create a working program first, and then substitute in better data structures.


Running the Program
-

To run the program, run the following console commands:

c++ tictactoeAI_driver.cpp tictactoeAI.cpp tictactoe.cpp

./a.out

Help
-

To choose which player makes the first move:

1 - Player moves first

2 - Computer moves first

To move, enter an integer 1-9:

+---+---+---+

|-1-|-2-|-3-|

+---+---+---+

|-4-|-5-|-6-|

+---+---+---+

|-7-|-8-|-9-|

+---+---+---+
