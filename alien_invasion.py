import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage assets and behaviour"""
    def __init__(self) -> None:
        "initialize the game, and create game resources"
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            0,0
        ), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Git rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_status = "right"
        elif event.key == pygame.K_LEFT:
            self.ship.moving_status = 'left'
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        """Respond to keyups"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.ship.moving_status = "stop"

    def _fire_bullet(self):
        """Create a new bullet and add it to the groups"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """Updates images on the screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()