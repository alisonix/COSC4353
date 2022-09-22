import enum
from enum import Enum, auto

class CellState(enum.Enum):
    ALIVE = True
    DEAD = False

def next_state(cell_status, number_of_live_neighbors):
  return number_of_live_neighbors == 3 or cell_status == CellState.ALIVE.value and number_of_live_neighbors == 2

def generate_signals_for_cell(cell): #2, 3
  # ((1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4))
  neighbor_signals = ((cell[0]-1, cell[1]-1), (cell[0]-1, cell[1]), (cell[0]-1, cell[1] + 1), (cell[0], cell[1]-1), (cell[0], cell[1]+1), (cell[0] + 1, cell[1] - 1), (cell[0]+1, cell[1]), (cell[0]+1, cell[1]+1))
  return neighbor_signals