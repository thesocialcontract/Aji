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

if __name__ == '__main__':
    unittest.main()
