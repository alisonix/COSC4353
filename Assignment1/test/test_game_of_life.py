import unittest

from src.gameoflife import *

DEAD = CellState.DEAD.value
ALIVE = CellState.ALIVE.value

class GameOfLifeTests(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)

    def test_dead_cell_behavior(self):
      number_of_live_neighbors_and_next_state = [(0, DEAD), (1, DEAD), (2, DEAD), (5, DEAD), (8, DEAD), (3, ALIVE)]
      for number_of_live_neighbors, next_cell_state in number_of_live_neighbors_and_next_state:
        with self.subTest(msg = "next_cell_state for number_of_live_neighbors", number_of_live_neighbors=number_of_live_neighbors):          
          self.assertEqual(next_cell_state, next_state(DEAD, number_of_live_neighbors))

    def test_live_cell_behavior(self):
      number_of_live_neighbors_and_next_state = [(1, DEAD), (4, DEAD), (8, DEAD), (3, ALIVE), (2, ALIVE)]
      for number_of_live_neighbors, next_cell_state in number_of_live_neighbors_and_next_state:
        with self.subTest(msg = "next_cell_state for number_of_live_neighbors", number_of_live_neighbors=number_of_live_neighbors):          
          self.assertEqual(next_cell_state, next_state(ALIVE, number_of_live_neighbors))
          
    def test_live_cell_at_2_3(self):
        cell = (2, 3)
        self.assertEqual(
            ((1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)),
            generate_signals_for_a_cell(cell))

    def test_live_cell_at_3_3(self):
        cell = (3, 3)
        self.assertEqual(
            ((2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)),
            generate_signals_for_a_cell(cell))

    def test_live_cell_at_2_4(self):
        cell = (2, 4)
        self.assertEqual(
            ((1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)),
            generate_signals_for_a_cell(cell))

    def test_live_cell_at_0_0(self):
        cell = (0, 0)
        self.assertEqual(((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
                          (1, 0), (1, 1)), generate_signals_for_a_cell(cell))

    def test_given_no_positions(self):
      cells = ()
      self.assertEqual([], generate_signals_for_multiple_cells(cells))

    def test_given_one_positions(self):
      cells = ((0, 0), )
      self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
                        generate_signals_for_multiple_cells(cells))
      
    def test_given_two_positions(self):
      cells = ((0, 0), (2, 3))
      self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), 
                        (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)], 
                        generate_signals_for_multiple_cells(cells))
      
    def test_given_three_positions(self):
      cells = ((0, 0), (2, 3), (3, 3))
      self.assertEqual([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), 
                        (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4), 
                        (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)],     
                        generate_signals_for_multiple_cells(cells))

    def test_count_live_neighbors_no_positions(self):
      cells = ()
      self.assertEqual({}, count_live_neighbors(cells))

    def test_count_live_neighbors_one_position(self):
      cells = ((0, 0), )
      self.assertEqual({(0, 0): 1}, count_live_neighbors(cells))

    def test_count_live_neighbors_two_position(self):
      cells = ((0, 0), (0, 0))
      self.assertEqual({(0, 0): 2}, count_live_neighbors(cells))
      
    def test_count_live_neighbors_three_position(self):
      cells = ((0, 0), (0, 1), (0, 0))
      self.assertEqual({(0, 0): 2, (0, 1): 1}, count_live_neighbors(cells))

    def test_block_compute_next_generation(self):
      cells = ((0, 0), (0, 1), (1, 0), (1, 1))
      self.assertEqual(((0, 0), (1, 1), (1, 0), (0, 1)), compute_next_generation(cells))
      
    def test_hive_compute_next_generation(self):
      cells = ((0,1), (1,0), (2, 0), (3, 1), (2, 2), (1, 2))
      self.assertEqual(((2, 2), (3, 1), (2, 0), (0, 1), (1, 2), (1, 0)), compute_next_generation(cells))

    def test_horizontal_blinker_compute_next_generation(self):
      cells = ((0, 0), (1, 0), (2, 0))
      self.assertEqual(((1, 1), (1, 0), (1, -1)), compute_next_generation(cells))

    def test_vertical_blinker_compute_next_generation(self):
      cells = ((1, 1), (1, 0), (1, -1))
      self.assertEqual(((2, 0), (1, 0), (0, 0)), compute_next_generation(cells))

    def test_glider_compute_next_generation(self):
      cells = ((1, 0), (2, 1), (2, 2), (1, 2), (0, 2))
      self.assertEqual(((1, 3), (2, 2), (1, 2), (2, 1), (0, 1)), compute_next_generation(cells))

if __name__ == '__main__':
    unittest.main()