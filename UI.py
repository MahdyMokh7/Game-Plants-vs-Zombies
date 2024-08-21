import pygame
import time
import math
from Time import Time
import os


class UI:

    START_PAGE_START_BAR_RECTANGLE_POSITION = rectangle_position = {
        "x_left_pos": 458,
        "x_right_pos": 738,
        "y_up_pos": 398,
        "y_down_pos": 485
    }

    # Image paths
    START_PAGE_IMAGE_PATH = os.path.join("Image files", "start_img.png")
    LAYOUT_PAGE_IMAGE_PATH = os.path.join("Image files", "layout_page_image1.png")
    IN_GAME_PAGE_IMAGE_PATH = os.path.join("Image files", "background_image.png")
    MENU_BAR_PAGE_IMAGE_PATH = os.path.join("Image files", "menu_bar_image1.png")

    # Page identifiers
    START_PAGE = "start_section"
    LAYOUT_PAGE = "layout_page"
    IN_GAME_PAGE = "in_game_page"
    MENU_BAR_PAGE = "menu_bar_page"

    # Messages
    WINNING_MESSAGE = "Congrats! You won :)"
    LOSING_MESSAGE = "HaHaHa! You lost :("

    def __init__(self, time, maap):
        self.time = time
        self.maap = maap
        self.current_page = None  # Track the current pages
        self.screen = None

    def __initialization(self):
        self.start_image = pygame.image.load(self.START_PAGE_IMAGE_PATH)
        self.start_image = pygame.transform.scale(self.start_image, (self.screen.get_width(), self.screen.get_height()))

        self.layout_image = pygame.image.load(self.LAYOUT_PAGE_IMAGE_PATH)
        self.layout_image = pygame.transform.scale(self.layout_image, (self.screen.get_width(), self.screen.get_height()))

        self.in_game_image = pygame.image.load(self.IN_GAME_PAGE_IMAGE_PATH)
        self.in_game_image = pygame.transform.scale(self.in_game_image, (self.screen.get_width(), self.screen.get_height()))

        self.menu_bar_image = pygame.image.load(self.MENU_BAR_PAGE_IMAGE_PATH)


    def set_up_window(self):
        """Set up the Pygame window and return the screen object."""
        self.screen = pygame.display.set_mode((1200, 700))  # Set the screen size to 1200x700
        pygame.display.set_caption("Plants vs Zombies")  # Set the window caption
        self.__initialization()
        self.current_page = UI.START_PAGE
        return self.screen

    def draw_timer(self):
        """Draw the timer in the upper right corner of the screen."""
        font = pygame.font.Font(None, 36)  # Use a built-in font with size 36
        current_time = self.time.get_current_time()
        minutes = current_time // 60
        seconds = current_time % 60
        time_str = f"{minutes:02}:{seconds:02}"  # Format as mm:ss
        text_surface = font.render(time_str, True, (255, 255, 255))  # White color text
        self.screen.blit(text_surface, (self.screen.get_width() - text_surface.get_width() - 10, 10))  # Draw in upper right

    def draw_start_page(self, screen):
        """Draw the start page background."""
        self.screen.blit(self.start_image, (0, 0))
        self.current_page = self.START_PAGE

    def draw_layout_page(self):
        """Draw the layout page background."""
        self.screen.blit(self.layout_image, (0, 0))
        self.current_page = self.LAYOUT_PAGE

    def draw_in_game_page(self):
        """Draw the in-game page background."""
        self.screen.blit(self.in_game_image, (0, 0))
        self.current_page = self.IN_GAME_PAGE

    def draw_menu_bar_page(self):
        """Draw the menu bar image on top of the current background without scaling."""
        image_rect = self.menu_bar_image.get_rect()
        
        x_position = (self.screen.get_width() - image_rect.width) // 2  # Center horizontally
        y_position = (self.screen.get_height() - image_rect.height) // 2  # Center vertically
        
        self.screen.blit(self.menu_bar_image, (x_position, y_position))
        self.current_page = self.MENU_BAR_PAGE

    def get_current_page(self):
        return self.current_page
    
    def set_current_page(self, page):
        self.current_page = page



if __name__ == "__main__":

    pygame.init()

    game_timer = Time()
    ui = UI(game_timer, 12)

    screen = ui.set_up_window()

    game_timer.start_time_counting()

    # Main Loop
    running = True
    clock = pygame.time.Clock()  # Initialize the clock for framerate control
    state = ui.get_current_page()  # Initial state to start with the start page
    timer_start = pygame.time.get_ticks()  # Timer to control the transition between pages
    delay = 5000  # 3-second delay for each page

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the elapsed time in milliseconds
        elapsed_time = pygame.time.get_ticks() - timer_start

        # Determine which page to show based on the elapsed time and state
        if state == UI.START_PAGE:
            ui.draw_start_page(screen)  # Draw the start page
            if elapsed_time > delay:
                state = UI.LAYOUT_PAGE  # Transition to layout page
                timer_start = pygame.time.get_ticks()  # Reset timer

        elif state == UI.LAYOUT_PAGE:
            ui.draw_layout_page(screen)  # Draw the layout page
            if elapsed_time > delay:
                state = UI.IN_GAME_PAGE  # Transition to in-game page
                timer_start = pygame.time.get_ticks()  # Reset timer

        elif state == UI.IN_GAME_PAGE:
            ui.draw_in_game_page(screen)  # Draw the in-game page
            ui.draw_menu_bar_page(screen)  # Draw the menu bar on top of the current page

        ui.draw_timer(screen)  # Draw the timer on the current page

        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Limit the frame rate to 60 FPS

    # Quit Pygame
    pygame.quit()
