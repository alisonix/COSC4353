import enum

class CellState(enum.Enum):
    ALIVE = True
    DEAD = False

def next_state(cell_status, number_of_live_neighbors):
  return number_of_live_neighbors == 3 or cell_status == CellState.ALIVE.value and number_of_live_neighbors == 2

def grid_status():
  return False