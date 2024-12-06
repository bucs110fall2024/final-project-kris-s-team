import pygame

class Lives:
    def __init__(self, x, y, max_lives, img="assets/heart.png"):
        self.x = x
        self.y = y
        self.lives = max_lives
        self.max_lives = max_lives
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (60, 60))
        
    def deduct(self):
        if self.lives > 0:
            self.lives -= 1
    def game_over(self):
        return self.lives <=0
    def reset(self):
        self.lives = self.max_lives
    def draw(self, screen):
        for i in range(self.lives):
            screen.blit(self.image, (self.x + i * 50, self.y))