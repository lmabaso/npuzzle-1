from npuzzle import NPuzzle
import heuristic

# unsolvable
# start = [5, 2, 7, 1, 3, 6, 0, 4, 8]
# easy
# start = [1, 2, 3, 8, 4, 5, 0, 7, 6]
start = [0, 1, 7, 6, 3, 4, 2, 5, 8]
# puzzle = NPuzzle(start, heuristic.hamming)
puzzle = NPuzzle(start, heuristic.manhattan)
puzzle.report()