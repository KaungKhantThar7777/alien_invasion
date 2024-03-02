import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # status for moving direction
        self.moving_status = "stop"
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_status == "right":
            self.rect.x += 1
        elif self.moving_status == 'left':
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)