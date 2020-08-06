from tests.fixtures import constants
from sgfmill import sgf

def load_input_sgf(test_file):
    filename = constants.test_input_filepath + test_file
    with open(filename, "r") as f:
        return sgf.Sgf_game.from_string(f.read())