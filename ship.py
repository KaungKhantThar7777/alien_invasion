import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # status for moving direction
        self.moving_status = "stop"
        
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_status == "right" and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_status == 'left' and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)