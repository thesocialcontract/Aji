import unittest

from sgfmill import sgf

from app import game
from app import game_sgf_io
from tests.fixtures import utils
from tests.fixtures import constants

class TestGameEquality(unittest.TestCase):
    """ Tests both test utils loading and conversion to Aji game object.
    """
    
    def setUp(self):
        self.go = game.Game(19)

    def test_compare_loaded_generated_equal(self):
        # Arrange
        loaded = utils.load_aji('input', 'equality-1')
        generated = self.go
        generated.place(constants.TOP_DOT_ROW,  constants.LEFT_DOT_COL)  # B
        generated.place(constants.TOP_DOT_ROW,  constants.RIGHT_DOT_COL) # W
        generated.place(constants.MID, constants.LEFT_DOT_COL) # B
        generated.place(constants.MID, constants.RIGHT_DOT_COL) # W
        
        # Act / Assert
        is_board_equal = generated._boards_equal(loaded._board) 
        self.assertTrue(is_board_equal)

    def test_generate_boards_equal_many_moves(self):
        # Arrange
        go1 = self.go
        go2 = game.Game(19)
        go1.place(0, 0)
        go1.place(0, 1)
        go2.place(0, 0)
        go2.place(0, 1)

        # Act / Assert
        is_board_equal = go1._boards_equal(go2._board)
        self.assertTrue(is_board_equal)

    def test_generate_boards_inequal(self):
        # Arrange
        go1 = self.go
        go2 = game.Game(19)
        go1.place(0, 0)
        go2.place(0, 1)

        # Act / Assert
        is_board_equal = go1._boards_equal(go2._board)
        self.assertFalse(is_board_equal)

if __name__ == '__main__':
    unittest.main()