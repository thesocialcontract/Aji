import unittest

from sgfmill import sgf

from app import aji
from tests.fixtures import utils

class TestSGF(unittest.TestCase):

    def test_sgf_read(self):
        # Arrange/Act/Assert
        # If no crash, test succeeds.
        test_input = "simple-place.sgf"
        test_sgf = utils.load_input_sgf(test_input)
        

if __name__ == '__main__':
    unittest.main()
