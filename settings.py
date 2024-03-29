class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        # screen
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230, 230)

        # ship settings
        self.ship_speed = 1.5

        # bullet
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        