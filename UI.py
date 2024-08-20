import pygame
import time
import math
from Time import Time
import os


class UI:

    START_PAGE_IAMGE_PATH = os.path.join("Image files" , "start_img.png")
    LAYOUT_PAGE_IMAGE_PATH = os.path.join("Image files", "layout_page_image1.png")
    iN_GAME_PAGE_IAMGE_PATH = os.path.join("Image files", "background_img.png")
    MENU_BAR_PAGE_IMAGE_PATH = os.path.join("Image files", "menu_bar_image.png")

    START_PAGE = "start_section"
    LAYOUT_PAGE = "layout_page"
    iN_GAME_PAGE = "in_game_page"
    MENU_BAR_PAGE = "menu_bar_page"

    WINNING_MESSAGE = "Congrats! You won :)"
    LOSSING_MESSAGE = "HaHaHa! You lost :("

    def __init__(self, time, maap):
        self.time = time
        self.maap = maap

    def draw_timer(self, screen):
        """Draw the timer in the upper right corner of the screen."""
        font = pygame.font.Font(None, 36)  # Use a built-in font with size 36
        current_time = self.time.get_current_time()
        print(current_time)
        minutes = current_time // 60
        seconds = current_time % 60
        time_str = f"{minutes:02}:{seconds:02}"  # Format as mm:ss
        text_surface = font.render(time_str, True, (255, 255, 255))  # White color text
        screen.blit(text_surface, (screen.get_width() - text_surface.get_width() - 10, 10))  # Draw in upper right


if __name__ == "__main__" :

    # Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set the screen size
    pygame.display.set_caption("Game Timer")
    clock = pygame.time.Clock()

    # Instantiate the classes
    game_timer = Time()
    ui = UI(game_timer, 12)

    # Start the timer
    game_timer.start_time_counting()

    # Main Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Clear screen with black
        ui.draw_timer(screen)  # Draw the timer
        
        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Limit the frame rate to 60 FPS

    # Quit Pygame
    pygame.quit()