import enum

class CellState(enum.Enum):
    ALIVE = True
    DEAD = False

def next_state(cell_status, number_of_live_neighbors):
  return number_of_live_neighbors == 3 or cell_status == CellState.ALIVE.value and number_of_live_neighbors == 2

def generate_signals_for_a_cell(cell):
  x = cell[0] 
  y = cell[1]
  return tuple((x + j, y + i)
    for j in range(-1, 2)
    for i in range (-1, 2)
    if not (x + j == x and y + i == y))

def generate_signals_for_multiple_cells(cells):
  return [item for i in [generate_signals_for_a_cell(x) for x in cells] for item in i]

def count_live_neighbors(cells):
  return {i: cells.count(i) for i in cells}

def compute_next_generation(cells):
  nextGen = [] 
  for j, k in count_live_neighbors(generate_signals_for_multiple_cells(cells)).items():
    Status = False
    if any(l == j for l in list(cells)): Status = True
    if (next_state(Status, k) == True): nextGen.insert(0, j)
  return tuple(nextGen)

  
  #return tuple([nextGen 
   #         for j, k in count_live_neighbors(generate_signals_for_multiple_cells(cells)).items()
    #          if any(l == j for l in list(cells)): Status = True
     #         if (next_state(Status, k) == True): nextGen.insert(0, j)])
