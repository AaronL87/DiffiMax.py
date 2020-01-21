# DiffiMax: The "Chess Trap Finder" Prototype
## A more human-useful version of Minimax


## This algorithm is essentially Minimax, but it chooses the second-best option for your opponent if there is enough of an evaluation difference between your opponent's first and second-best options and there are a substantial number of move choices on your opponent's turn. That is, it prioritizes traps by assuming that your opponent will make a mistake but that, if they get it correct, your evaluation is still in the "drawish range."

### It is primarily useful if there is no clear winning variation (pure MiniMax yields no clear win) but that one wants to find positions where your opponent has a low probability of randomly picking the best choice, thereby acting as a kind of trap-finding chess second.

## In order to avoid forced moves that aren't traps, it only considers moves that aren't a check or capture/recapture.

## There are other conditions that can be added for what constitutes a trap candidate, like weighing the trap evaluation difference based on the number of moves in the position.

## This algorithm can be optimized because only first and second-best options need to be chosen, so all of the children don't need to be sorted.

## This can be further optimized using alpha-beta pruning on the half of choices that you make and an alternative alpha-beta pruning on your opponent's choices. I will be working on that alternative ongoingly.
