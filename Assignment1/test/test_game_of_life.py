import unittest

#from src.gameoflife import GameOfLife
from src.gameoflife import Cell

class GameOfLifeTests(unittest.TestCase):
  def test_Canary(self):
    self.assertTrue(True)

  def test_Cell_exists(self):
    self.assertTrue(True)

  def test_Cell_is_Alive(self):
    Cell.status = True
    self.assertEqual(True, Cell().isAlive())

  def test_Cell_is_Dead(self):
    Cell.status = False
    self.assertEqual(False, Cell().isAlive())

if __name__ == '__main__': 
  unittest.main()