from sgfmill import sgf

from app import game

def build_game_from_sgf(filename):
    with open(filename, "r") as f:
        sgf_data = sgf.Sgf_game.from_string(f.read())

    go = game.Game(sgf_game=sgf_data)
    return go