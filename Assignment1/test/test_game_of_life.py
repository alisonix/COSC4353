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

    def test_live_cell_at_2_3(self):
        cell = (2, 3)
        self.assertEqual(
            ((1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)), generate_signals_for_cell(cell))

    def test_live_cell_at_3_3(self):
        cell = (3, 3)
        self.assertEqual(
            ((2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)), generate_signals_for_cell(cell))

    def test_live_cell_at_2_4(self):
        cell = (2, 4)
        self.assertEqual(
            ((1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)), generate_signals_for_cell(cell))

    def test_live_cell_at_0_0(self):
        cell = (0, 0)
        self.assertEqual(((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)), generate_signals_for_cell(cell))


if __name__ == '__main__':
    unittest.main()
