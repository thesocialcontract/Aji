from app import game

class Aji:
    def __init__(self):
        pass

    def start_new_game(self, size=19):
        self.game = game.Game(size)
        return self.game

if __name__ == "__main__":
    print("Hello Initial Commit")