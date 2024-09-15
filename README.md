# DiffiMax: The Chess Trap Finder

## Overview

DiffiMax is an enhanced version of the Minimax algorithm, designed to identify "traps" in chess. Instead of always choosing the optimal move, DiffiMax considers the likelihood that your opponent will make a mistake. It prioritizes moves that could exploit potential errors by the opponent, even if the overall evaluation of the position is less clear.

### Key Features

- **Trap-Finding:** Targets moves that are less likely to be countered correctly by the opponent, potentially leading to advantageous positions even in uncertain situations.
- **Human-Usefulness:** Focuses on practical applications for human players, especially in scenarios where pure Minimax does not yield a clear winning strategy.
- **Optimizations:** Includes considerations for moves that are not forced (i.e., not checks or captures) and is designed to be optimized with alpha-beta pruning.

### Usage

1. Clone the repository: `git clone https://github.com/YourUsername/ChessTrapFinder.git`
2. Navigate to the project directory.
3. Open the notebook: `ChessTrapAlgo.ipynb` in Jupyter Notebook or any compatible environment.

### Future Work

- **Alpha-Beta Pruning:** Additional optimizations using alpha-beta pruning to enhance performance.
- **Trap Criteria:** Further development to refine the criteria for identifying trap candidates.
