import unittest

from sgfmill import sgf

from app import aji
from app import game
from tests.fixtures import utils

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game_test = aji.start_new_game()
        pass

    def test_game_starts(self):
        is_valid_game = type(self.game_test) is game.Game # Arrange / Act
        self.assertTrue(is_valid_game)  # Assert

    def test_game_can_place(self):
        # Arrange
        self.game_test.place(0, 0)            # Act / Assert

    def test_game_can_read(self):
        # Arrange
        self.game_test.place(0, 0)
        
        # Act
        result = self.game_test.get(0, 0)

        # Assert
        expected = 'b'
        self.assertEqual(result, expected)

    def test_game_switch_players(self):
        self.assertEqual(self.game_test.current_player, 'b')
        self.game_test._switch_player()
        self.assertEqual(self.game_test.current_player, 'w')

    def test_game_cur_player_switches_on_place(self):
        # Arrange
        initial = self.game_test.current_player
        
        # Act
        self.game_test.place(0, 0)

        # Assert
        result = self.game_test.current_player
        initial_expected = 'b'
        expected = 'w'
        self.assertEqual(initial, initial_expected)
        self.assertEqual(result, expected)
        
    def test_game_place_out_of_bounds(self):
        # Arrange / Act / Assert
        with self.assertRaises(IndexError):
            self.game_test.place(-1,0)

    def test_game_place_preoccupied_space(self):
        # Arrange
        self.game_test.place(0,0)
        
        # Act / Assert
        with self.assertRaises(ValueError):
            self.game_test.place(0,0)
    
    def test_game_players_place_many(self):
        # Arrange / Act
        # TODO: place a bunch
        # Assert
        # TODO: Load expected sgf
        # TODO: Make expected sgf
        # TODO: Assert board == expected
        pass

    def test_game_can_end(self):
        self.game_test.end_and_report() # Arrange/Act/Assert

    def test_game_score_empty_board(self):
        # Arrange / Act
        result = self.game_test.end_and_report()
        expected = -8    #  Komi.  Possible refactor candidate in testing? Pass a 'rules' object?
        # Assert
        self.assertEqual(result, expected)

    def test_game_score_both_on_board(self):
        # Arrange
        self.game_test.place(0,0)
        self.game_test.place(0,1)

        # Act
        result = self.game_test.end_and_report()

        # Assert
        expected = -8    # Equal number
        self.assertEqual(result, expected)

    def test_game_score_black_wins(self):
        # Arrange
        for i in range(0, 10):
            self.game_test.place(0,i)
        # Act
        result = self.game_test.end_and_report()

        # Assert
        expected = 2
        self.assertEqual(result, expected)

    def test_game_score_white_wins(self):
        pass

    def test_game_score_with_captured(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
