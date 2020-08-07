from sgfmill import sgf

from app import game

def build_game_from_sgf(filename):
    with open(filename, "r") as f:
        sgf_data = sgf.Sgf_game.from_string(f.read())
    
    loaded_size = sgf_data.get_size()
    go = game.Game(size=loaded_size)
    return go


# def load_from_file(self, filename):
#     """ Doesn't make sense as a Game Object
#     """
#     with open(filename, "r") as f:
#         sgf_data = sgf.Sgf_game.from_string(f.read())
#     self.board.