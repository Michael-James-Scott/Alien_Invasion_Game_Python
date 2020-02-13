import sys
import pygame as pg
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
        
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pg.display.flip()

    def _check_events(self):
        # Respond to keyboard and mouse events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit() 

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()