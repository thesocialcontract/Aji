import unittest

from sgfmill import sgf

from app import aji
from app import game
from app import game_sgf_io
from tests.fixtures import utils
from tests.fixtures import constants

class TestGameSgfIo(unittest.TestCase):
    """ Tests both test utils loading and conversion to Aji game object.
    """
    
    def setUp(self):
        self.go = aji.start_new_game()

    def test_load_empty(self):
        # Arrange / Act (utils.load_aji calls game_sgf_io.build_game_from_sgf)
        loaded_go = utils.load_aji('input', 'empty')
        fresh_go = self.go

        self.assertEqual(self.go._current_player, loaded_go._current_player)
        self.assertEqual(self.go.size, loaded_go.size)

        are_boards_equal = fresh_go._boards_equal(loaded_go._board)
        self.assertTrue(are_boards_equal)
        self.assertTrue(fresh_go._board.is_empty())

    def test_load_1_good_move(self):
        # Arrange / Act
        # utils.load_aji will call game_sgf_io.build_game_from_sgf
        # which is what we're testing.
        loaded_go = utils.load_aji('input', 'one-good')
        generated_go = self.go
        generated_go.place(constants.TOP_DOT_ROW, constants.LEFT_DOT_COL)

        # Assert
        are_boards_equal = generated_go._boards_equal(loaded_go._board)
        self.assertTrue(are_boards_equal)

if __name__ == '__main__':
    unittest.main()

