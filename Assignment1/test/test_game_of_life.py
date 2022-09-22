import unittest

from src.gameoflife import *

DEAD = CellState.DEAD.value
ALIVE = CellState.ALIVE.value

class GameOfLifeTests(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)

    def test_dead_cell_dead_no_neighbors(self):
        cell_status = DEAD
        number_of_live_neighbors = 0
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_dead_cell_dead_one_neighbor(self):
        cell_status = DEAD
        number_of_live_neighbors = 1
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_dead_cell_dead_two_neighbors(self):
        cell_status = DEAD
        number_of_live_neighbors = 2
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_dead_cell_dead_five_neighbors(self):
        cell_status = DEAD
        number_of_live_neighbors = 5
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_dead_cell_dead_eight_neighbors(self):
        cell_status = DEAD
        number_of_live_neighbors = 8
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_dead_cell_alive_three_neighbors(self):
        cell_status = DEAD
        number_of_live_neighbors = 3
        self.assertEqual(ALIVE, next_state(cell_status, number_of_live_neighbors))

    def test_live_cell_dead_one_neighbor(self):
        cell_status = ALIVE
        number_of_live_neighbors = 1
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_live_cell_dead_four_neighbors(self):
        cell_status = ALIVE
        number_of_live_neighbors = 4
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_live_cell_dead_eight_neighbors(self):
        cell_status = ALIVE
        number_of_live_neighbors = 8
        self.assertEqual(DEAD, next_state(cell_status, number_of_live_neighbors))

    def test_live_cell_live_three_neighbors(self):
        cell_status = ALIVE
        number_of_live_neighbors = 3
        self.assertEqual(ALIVE, next_state(cell_status, number_of_live_neighbors))

    def test_live_cell_live_two_neighbors(self):
      cell_status = ALIVE
      number_of_live_neighbors = 2
      self.assertEqual(ALIVE, next_state(cell_status, number_of_live_neighbors))

    def test_grid_does_not_exist(self):
      self.assertEqual(False, grid_status())

if __name__ == '__main__':
    unittest.main()