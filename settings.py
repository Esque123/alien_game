class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # fulscreen_mode(True)

        # Ship settings
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

    # def fullscreen_mode(self, value):
    #     """ Enable or disable fullscreen """
    #     if value == True:
    #         # Full screen
    #         self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #         self.settings.screen_width = self.screen.get_rect().width
    #         self.settings.screen_height = self.screen.get_rect().height
    #     else:
    #         self.screen = pygame.display.set_mode(
    #             (self.settings.screen_width, self.settings.screen_height))
