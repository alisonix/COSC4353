import unittest

from src.gameoflife import GameOfLife

class GameOfLifeTests(unittest.TestCase):
  def test_Canary(self):
    self.assertTrue(True)

  def test_example_remove_this(self):
    self.assertEqual(1, GameOfLife().please_remove_this_sample())

if __name__ == '__main__': 
  unittest.main()
