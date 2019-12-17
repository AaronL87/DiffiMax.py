# DiffiMax
## A more practical and human-useful version of the MiniMax game algorithm

My original intention was to use this algorithm in opening preparation as a "trap finder."

Rather than having a chess engine (or other turn-based game engine) pick the objectively optimal choice, this algorithm will sacrifice one player's evaluation within "drawish" boundaries in order to make things as difficult as possible for your opponent.
This will be done by picking lines with numerous, unforced options that also have the biggest difference between the first-best and second-best moves. 

In order for the choices to be unforced, the moves could not involve a recapture.

Lines with multiple only-move positions in them will be given precedence.
Following the simple implementation of this algorithm, I will include weighing in other factors that determine the human-level complexity of a position.

Because only the opponent's moves are considered by this metric, the player's choices involve a version of MiniMax that restarts from the last "trap move" if a line where the player stays above the draw threshold isn't found.
