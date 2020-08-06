from sgfmill import boards
from sgfmill import common

class Game:
    def __init__(self, size=19):
        self.size = 19
        self.board = boards.Board(size)
        self.black = 'b'
        self.white = 'w'
        self.current_player = 'b'
        self.komi = 8
        
    def _switch_player(self):
        if self.current_player == self.black:   # This logic isn't helpful at all, adds more tests, and I'll have to rewrite in the future anyway.
            self.current_player = self.white
        else:
            self.current_player = self.black

    def place(self, x, y):
        self.board.play(x, y, self.black)
        self._switch_player()
        pass

    def get(self, x, y):
        return self.board.get(x, y)

    def end_and_report(self):
        return self.board.area_score() - self.komi
