import unittest

from sgfmill import sgf

from app import aji
from app import game
from tests.fixtures import utils

class TestGame(unittest.TestCase):

    def setUp(self):
        self.go = aji.start_new_game()
        pass

    def test_game_starts(self):
        is_valid_game = type(self.go) is game.Game # Arrange / Act
        self.assertTrue(is_valid_game)  # Assert

    def test_game_can_place(self):
        # Arrange
        self.go.place(0, 0)            # Act / Assert

    def test_game_can_read(self):
        # Arrange
        self.go.place(0, 0)
        
        # Act
        result = self.go.get(0, 0)

        # Assert
        expected = 'b'
        self.assertEqual(result, expected)

    def test_game_switch_players(self):
        self.assertEqual(self.go._current_player, 'b')
        self.go._switch_player()
        self.assertEqual(self.go._current_player, 'w')

    def test_game_cur_player_switches_on_place(self):
        # Arrange
        initial = self.go._current_player
        
        # Act
        self.go.place(0, 0)

        # Assert
        result = self.go._current_player
        initial_expected = 'b'
        expected = 'w'
        self.assertEqual(initial, initial_expected)
        self.assertEqual(result, expected)
        
    def test_game_place_out_of_bounds(self):
        # Arrange / Act / Assert
        with self.assertRaises(IndexError):
            self.go.place(-1,0)

    def test_game_place_preoccupied_space(self):
        # Arrange
        self.go.place(0,0)
        
        # Act / Assert
        with self.assertRaises(ValueError):
            self.go.place(0,0)
            
    def test_game_can_end(self):
        self.go.end_and_report() # Arrange/Act/Assert

    def test_game_score_empty_board(self):
        # Arrange / Act
        result = self.go.end_and_report()
        expected = -8    #  Komi.  Possible refactor candidate in testing? Pass a 'rules' object?
        # Assert
        self.assertEqual(result, expected)

    def test_game_score_both_on_board(self):
        # Arrange
        self.go.place(0,0)
        self.go.place(0,1)

        # Act
        result = self.go.end_and_report()

        # Assert
        expected = -8    # Equal number
        self.assertEqual(result, expected)

    def test_game_score_black_wins(self):
        # Arrange
        for i in range(0, 10):
            self.go.place(0,i)
        # Act
        result = self.go.end_and_report()
        # Assert
        expected = 13
        #self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

