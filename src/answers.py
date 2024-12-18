import pygame

class Answers:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
    
    def draw(self, screen):
        """
        This method draws the answer buttons on the screen.
        args: screen that is being drawn on
        returns: none
        """
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
        
    def click(self, event):
        """
        This method determines if an answer button has been clicked.
        args: event, if a button is clicked
        Returns: bool value for whether or not a button is clicked
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    