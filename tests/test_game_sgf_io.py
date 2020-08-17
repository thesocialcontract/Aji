import unittest

from sgfmill import sgf

from app import game
from app import game_sgf_io
from tests.fixtures import utils
from tests.fixtures import constants

class TestGameSgfIo(unittest.TestCase):
    """ Tests both test utils loading and conversion to Aji game object.
    """
    
    def setUp(self):
        self.go = game.Game(19)

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

    def test_save_empty(self):
        # Arrange
        generated_sgf = self.go._sgf
        save_file = constants.test_results_filepath + "save-empty.sgf"

        # Act / Assert (Passes if no exception)
        game_sgf_io.save_sgf(generated_sgf, save_file)

        # To think about: io doesn't matter in somethign this small
        #        but will io slow testing when the codebase is large?

    def test_save_1_good_move(self):
        # Arrange
        generated_game = self.go

        # Act
        generated_game.place(0,0)
        generated_sgf = generated_game._sgf
        save_file = constants.test_results_filepath + "save-1-good.sgf"
        game_sgf_io.save_sgf(generated_sgf, save_file)

        # Assert
        expected = constants.SIMPLE_SGF
        result = game_sgf_io.sgf_to_str(generated_sgf)
        self.assertEqual(result, expected)

    def test_save_fails_invalid_path(self):
        # Arrange
        generated_sgf = self.go._sgf
        save_file = "/asdf/f///faaw/ef/awe//save-empty.sgf"

        # Act / Assert
        with self.assertRaises(Exception):
            game_sgf_io.save_sgf(generated_sgf, save_file)

    def test_save_full_game(self):
        pass

    def test_saved_loads_same(self):
        pass

if __name__ == '__main__':
    unittest.main()

