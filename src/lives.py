import from assets 

class Lives:
    def __init__(self, lives=3):
        self.lives = lives
        self.x = 0
        self.y = 0
        self.image = heart.jpg
    def deduct(self):
        self.lives -= 1
    def game_over(self):
        if self.lives == 0:
            exit()