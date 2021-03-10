from enum import Enum

class Difficulty(Enum):
    easy = "easy"
    normal = "normal"
    hard = "hard"


class Mario:

    def __init__(self, difficulty, lives):
        self.difficulty = difficulty
        self.lives = lives

    def die(self):
        self.lives -= 1
    
    def change_difficulty(self, difficulty: Difficulty):
        self.difficulty = difficulty
        