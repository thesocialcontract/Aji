from sgfmill import sgf
from sgfmill import boards
from sgfmill import common
from sgfmill import ascii_boards

class Game:
    def __init__(self, size=19, sgf_game=None):
        if sgf_game is not None:
            self._load_sgf(sgf_game)
        else:
            self._current_player = 'b'
            self.komi = 8
            self.size = size
            self._board = boards.Board(size)


    def _load_sgf(self, sgf_game):
        self._sgf = sgf_game
        self.size = sgf_game.get_size()
        self.komi = sgf_game.get_komi()
        self._board = boards.Board(self.size)

        # Load Moves
        moves = sgf_game.get_main_sequence()
        if len(moves) == 1: # We're empty, no nodes to run
            self._current_player = 'b'
            return

        # Tree Node get_move returns tuple ( color, (x, y) )
        first_move = moves[1].get_move()
        self._current_player = first_move[0]
        for node in moves[1:]:
            move = node.get_move()
            if not move:
                continue
            x = move[1][0]
            y = move[1][1]
            color = move[0]
            self.place(x,y) # TODO: Allow for inital placements?

    def _boards_equal(self, board):
        """ Deep equality check to see if boards are the same.
        """
        if board.side != self.size:
            return False

        return self._board.list_occupied_points() == board.list_occupied_points()
        
    def _switch_player(self):
        black = 'b'
        white = 'w'
        if self._current_player == black:   # This logic isn't helpful at all, adds more tests, and I'll have to rewrite in the future anyway.
            self._current_player = white
        else:
            self._current_player = black

    def place(self, x, y):
        self._board.play(x, y, self._current_player)
        self._switch_player()
        pass

    def get(self, x, y):
        return self._board.get(x, y)

    def end_and_report(self):
        return self._board.area_score() - self.komi

    def __str__(self):
        result = ascii_boards.render_board(self._board)
        player = "Black" if self._current_player == 'b' else "White"
        result += "\n"
        result += f"Current Player: {player}"
        return result