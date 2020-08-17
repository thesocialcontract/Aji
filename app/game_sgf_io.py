from sgfmill import sgf

from app import game

def build_game_from_sgf(filename):
    with open(filename, "r") as f:
        sgf_data = sgf.Sgf_game.from_string(f.read())

    go = game.Game(sgf_game=sgf_data)
    return go

def sgf_to_str(sgf_game):
    sgf_bytes = sgf_game.serialise()
    return sgf_bytes.decode('utf-8')

def save_sgf(sgf_game, filename):    
    content = sgf_to_str(sgf_game)
    with open(filename, 'w') as f:
        f.write(content)