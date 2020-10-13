from sgfmill import sgf
from sgfmill import boards
from sgfmill import common
from sgfmill import ascii_boards

class Game:
    """
        Game handles gamestate logic for Go.  It has a board, a set of rules to play, 
        and an SGF tree keeping track of game state.
    """
    def __init__(self, size=19, sgf_game=None):
        if sgf_game is not None:
            self._load_sgf(sgf_game)
        else:
            self._sgf = sgf.Sgf_game(size)
            self._current_player = 'b'
            self.komi = 8
            self.size = size
            self._board = boards.Board(size)

    def _load_sgf(self, sgf_game):
        self._sgf = sgf_game
        self.size = sgf_game.get_size()
        self.komi = sgf_game.get_komi()
        self._board = boards.Board(self.size)

        # HACK: This is extremely coupled with SGFMill.  Don't like.
        # NOTE: Consider moving SGF operations to an SGF Mediator
        last_node = sgf_game.get_last_node()
        last_player = last_node.get_move()[0]
        if last_player:
            self._current_player = last_player
            self._switch_player()
        else:
            self._current_player = 'b'  # Default to black

        # Load Moves
        moves = sgf_game.get_main_sequence()
        if len(moves) == 1: # We're empty, no nodes to run.  Why 1?
            self._current_player = 'b'
            return

        # Tree Node get_move returns tuple ( color, (x, y) )
        first_move = moves[1].get_move()
        self._current_player = first_move[0]
        for node in moves[1:]:
            move = node.get_move()
            if not move:
                continue
            x = move[1][0] # ( color, (x,y) ) -> (x,y) -> (x)
            y = move[1][1] # ( color, (x,y) ) -> (x,y) -> (y)
            color = move[0]
            self._board.play( x, y, color )
        
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

    def place(self, row, col):
        """ 
            Place the current player's stone at the given location.
            TODO: Consider adding player to authenticate player placement.
            TODO: Add invalid placement errors.
            TODOs never get completed unless marked in planning space.
            
        """
        # Place
        self._board.play( row, col, self._current_player )

        # Record in SGF.  SGF Tree is mutable.
        next_node = self._sgf.extend_main_sequence()
        next_node.set_move( self._current_player, (row, col) )

        self._switch_player()

    def get(self, x, y):
        return self._board.get(x, y)

    def end_and_report(self):
        return self._board.area_score() - self.komi

    def __str__(self):
        player = "Black" if self._current_player == 'b' else "White"
        board = ascii_boards.render_board(self._board)
        result  = f"{board}\n"
        result += f"Current Player: {player}"
        return result