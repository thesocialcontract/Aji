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
        # Arrange
        input_filepath = constants.test_input_filepath + "empty.sgf"

        # Act
        test_go = game_sgf_io.build_game_from_sgf(input_filepath)

        self.assertEqual(self.go.current_player, test_go.current_player)
        self.assertEqual(self.go.size, test_go.size)
        # SGF Boards compare object references instead of values in board.
        #self.assertEqual(self.go.board, test_go.board)
        self.assertTrue(test_go.board.is_empty())

    def test_load_1_good_move(self):
        # Arrange
        input_filepath = constants.test_input_filepath + "one-good.sgf"

        # Act
        test_go = game_sgf_io.build_game_from_sgf(input_filepath)

        # Assert
        self.assertEqual(self.go.current_player, test_go.current_player)
        self.assertEqual(self.go.size, test_go.size)
        # START HERE
        # TODO: Find an elegant way to verify board equality.
        # You're not really going to need it in any other place except
        # in test classes, and in checking old board states.

if __name__ == '__main__':
    unittest.main()

