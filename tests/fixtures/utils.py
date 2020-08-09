from sgfmill import sgf
from app import game_sgf_io
from tests.fixtures import constants

_fixture_filepaths = {
    "input": constants.test_input_filepath,
    "expected": constants.test_expected_filepath
}

def report_games(game_loaded, game_generated):
    """ For debugging in tests.
    e.g. making sure generated tests are what you're expecting
    """
    print('')
    print("------------------------------------------------")
    print("LOADED")
    print(game_loaded)
    print("------------------------------------------------")
    print("GENERATED")
    print(game_generated)

def load_input_sgf(test_file):
    """ Basic load input.  Do not use"""
    filename = constants.test_input_filepath + test_file
    with open(filename, "r") as f:
        return sgf.Sgf_game.from_string(f.read())

def load_aji(fixture_type, test_file):
    """ Builds aji game from game_sgf_io util and test fixture constants. 
    """
    if fixture_type not in _fixture_filepaths:
        raise ValueError("Invliad Test Fixture Type")

    filename = constants.test_input_filepath + test_file + ".sgf"
    with open(filename, "r") as f:
        return game_sgf_io.build_game_from_sgf(filename)