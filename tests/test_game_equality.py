import unittest

from sgfmill import sgf

from app import aji
from app import game
from app import game_sgf_io
from tests.fixtures import utils
from tests.fixtures import constants

class TestGameEquality(unittest.TestCase):
    """ Tests both test utils loading and conversion to Aji game object.
    """
    
    def setUp(self):
        self.go = aji.start_new_game()

    def test_compare_loaded_generated_equal(self):
        # Arrange
        loaded = utils.load_aji('input', 'equality-1')
        generated = self.go
        generated.place(constants.top_dot_row,  constants.left_dot_col)  # B
        generated.place(constants.top_dot_row,  constants.right_dot_col) # W
        generated.place(9, constants.left_dot_col) # B
        generated.place(9, constants.right_dot_col) # W
        
        # Act / Assert
        is_board_equal = generated._boards_equal(loaded._board) 
        self.assertTrue(is_board_equal)

    def test_generate_boards_equal_many_moves(self):
        # Arrange
        go1 = self.go
        go2 = aji.start_new_game()
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
        go2 = aji.start_new_game()
        go1.place(0, 0)
        go2.place(0, 1)

        # Act / Assert
        is_board_equal = go1._boards_equal(go2._board)
        self.assertFalse(is_board_equal)

if __name__ == '__main__':
    unittest.main()