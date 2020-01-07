# DiffiMax: The "Chess Trap Finder" Prototype
## A more human-useful version of Minimax


## This algorithm is essentially Minimax, but it chooses the second-best option for your opponent if there is enough of an evaluation difference between your opponent's first and second-best options and there are a substantial number of move choices on your opponent's turn. That is, it prioritizes traps by assuming that your opponent will make a mistake but that, if they get it correct, your evaluation is still in the "drawish range." 

## In order to avoid forced moves that aren't traps, it only considers moves that aren't a check or capture/recapture.

## There are other conditions that can be added for what constitutes a trap candidate, like weighing the trap evaluation difference based on the number of moves in the position.

## Algorithm can be optimized because only first and second-best options need to be chosen, so all of the children don't need to be sorted.
