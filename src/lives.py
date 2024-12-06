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
        """
        This method deducts a life from the total lives.
        args: none
        returns: none
        """
        if self.lives > 0:
            self.lives -= 1
    def game_over(self):
        """
        This method determines that the game is over when the lives are gone.
        args: none
        Returns: int
        """
        return self.lives <=0
    def reset(self):
        """
        This method resets the number of lives.
        args: none
        return: none
        """
        self.lives = self.max_lives
    def draw(self, screen):
        """
        This method draws the lives on the screen.
        args: screen that is being drawn on
        returns: none
        """
        for i in range(self.lives):
            screen.blit(self.image, (self.x + i * 50, self.y))