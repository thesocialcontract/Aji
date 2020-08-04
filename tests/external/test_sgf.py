import unittest

from sgfmill import sgf

from app import aji
from tests.fixtures import constants

class TestSGF(unittest.TestCase):

    def test_sgf_read(self):
        # Arrange
        test_input = constants.test_input_filepath + "simple-place.sgf"
        with open(test_input, "rb") as f:
            game = sgf.Sgf_game.from_bytes(f.read())
        # If no crash, then test succeeds

    def test_


if __name__ == '__main__':
    unittest.main()

"""Sgfmill represents Go colours and moves as follows:
Name 	Possible values
colour 	single-character string: 'b' or 'w'
point 	pair (int, int) of coordinates
move 	point or None (for a pass)

The terms colour, point, and move are used as above throughout this documentation (in particular, when describing parameters and return types).

colour values are used to represent players, as well as stones on the board. (When a way to represent an empty point is needed, None is used.)

point values are treated as (row, column). The bottom left is (0, 0) (the same orientation as GTP, but not SGF). So the coordinates for a 9x9 board are as follows:

9 (8,0)  .  .  .  .  .  (8,8)
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1 (0,0)  .  .  .  .  .  (0,8)
   A  B  C  D  E  F  G  H  J

"""