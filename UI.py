import pygame
import time
import math
from Time import Time
import os
import sys 

class UI:

    START_PAGE_START_BAR_RECTANGLE_POSITION = {
        "x_left_pos": 458,
        "x_right_pos": 738,
        "y_up_pos": 398,
        "y_down_pos": 485
    }
    LAYOUT_PAGE_ADVENTURE_BAR_RECTANGLE_POSITION = {
        "x_left_pos": 615,
        "x_right_pos": 1084,
        "y_up_pos": 96,
        "y_down_pos": 228
    }
    LAYOUT_PAGE_QUIT_BAR_RECTANGLE_POSITION = {
        "x_left_pos": 1065,
        "x_right_pos": 1165,
        "y_up_pos": 560,
        "y_down_pos": 630
    }
    LAYOUT_PAGE_OPTIONS_BAR_RECTANGLE_POSITION = {
        "x_left_pos": 846,
        "x_right_pos": 959,
        "y_up_pos": 550,
        "y_down_pos": 607
    }
    MENU_PAGE_CONTINUE_BAR_RECTABGLE_POSITION = {
        "x_left_pos": 518,
        "x_right_pos": 671,
        "y_up_pos": 408,
        "y_down_pos": 479
    }
    MENU_PAGE_MUTE_BAR_RECTABGLE_POSITION = {
        "x_left_pos": 521,
        "x_right_pos": 671,
        "y_up_pos": 233,
        "y_down_pos": 284
    }
    MENU_PAGE_SPEED_BAR_RECTABGLE_POSITION = {
        "x_left_pos": 521,
        "x_right_pos": 671,
        "y_up_pos": 301,
        "y_down_pos": 352
    }
    IN_GAME_PAGE_MENU_BAR = {
        "x_left_pos": 1025,
        "x_right_pos": 1200,
        "y_up_pos": 0,
        "y_down_pos": 67
    }
    # IN_GAME_PAGE_SUN_BAR = {
    #     "x_left_pos": 170,
    #     "x_right_pos": 306,
    #     "y_up_pos": 12,
    #     "y_down_pos": 56
    # }
    IN_GAME_PAGE_MENU_BAR = {
        "x_left_pos": 1025,
        "x_right_pos": 1200,
        "y_up_pos": 1,
        "y_down_pos": 66
    }
    IN_GAME_PAGE_SUN_BAR = {
        "x_left_pos": 170,
        "x_right_pos": 303,
        "y_up_pos": 12,
        "y_down_pos": 54
    }
    IN_GAME_PAGE_SUNFLOWER_BAR = {
        "x_left_pos": 2,
        "x_right_pos": 87,
        "y_up_pos": 4,
        "y_down_pos": 121
    }
    IN_GAME_PAGE_PEASHOOTER_BAR = {
        "x_left_pos": 2,
        "x_right_pos": 87,
        "y_up_pos": 126,
        "y_down_pos": 248
    }
    IN_GAME_PAGE_SNOWPEASHOOTER_BAR = {
        "x_left_pos": 2,
        "x_right_pos": 87,
        "y_up_pos": 253,
        "y_down_pos": 372
    }
    IN_GAME_PAGE_SIBZAMINI_BAR = {
        "x_left_pos": 2,
        "x_right_pos": 87,
        "y_up_pos": 376,
        "y_down_pos": 496
    }
    IN_GAME_PAGE_TIMER_BAR = {
        "x_left_pos": 855,
        "x_right_pos": 1016,
        "y_up_pos": 2,
        "y_down_pos": 66
    }


    # Image paths
    START_PAGE_IMAGE_PATH = os.path.join("Image files", "start_img.png")
    LAYOUT_PAGE_IMAGE_PATH = os.path.join("Image files", "layout_page_image1.png")
    IN_GAME_PAGE_IMAGE_PATH = os.path.join("Image files", "background_completed_img.png")
    MENU_BAR_PAGE_IMAGE_PATH = os.path.join("Image files", "menu_bar_image5.png")
    VICTORY_PAGE_IMAGE_PATH = os.path.join("Image files", "Victory.png")
    LOST_PAGE_IMAGE_PATH = os.path.join("Image files", "Game Over Screen1.png")

    # Page identifiers
    START_PAGE = "start_section"
    LAYOUT_PAGE = "layout_page"
    IN_GAME_PAGE = "in_game_page"
    MENU_BAR_PAGE = "menu_bar_page"
    VICTORY_PAGE = "victory"
    LOST_PAGE = "lost_page"

    # Messages
    WINNING_MESSAGE = "Congrats! You won :)"
    LOSING_MESSAGE = "HaHaHa! You lost :("

    def __init__(self, time, maap):
        self.time = time
        self.maap = maap
        self.current_page = None  # Track the current page
        self.prev_page = None  # Tarck the previous page
        self.screen = None

    def __initialization(self):
        self.start_image = pygame.image.load(self.START_PAGE_IMAGE_PATH)
        self.start_image = pygame.transform.scale(self.start_image, (self.screen.get_width(), self.screen.get_height()))

        self.layout_image = pygame.image.load(self.LAYOUT_PAGE_IMAGE_PATH)
        self.layout_image = pygame.transform.scale(self.layout_image, (self.screen.get_width(), self.screen.get_height()))

        self.in_game_image = pygame.image.load(self.IN_GAME_PAGE_IMAGE_PATH)
        self.in_game_image = pygame.transform.scale(self.in_game_image, (self.screen.get_width(), self.screen.get_height()))

        self.victory_image = pygame.image.load(self.VICTORY_PAGE_IMAGE_PATH)
        # self.victory_image = pygame.transform.scale(self.victory_image, (self.screen.get_width(), self.screen.get_height()))

        self.lost_image = pygame.image.load(self.LOST_PAGE_IMAGE_PATH)
        # self.lost_image = pygame.transform.scale(self.lost_image, (self.screen.get_width(), self.screen.get_height()))

        self.menu_bar_image = pygame.image.load(self.MENU_BAR_PAGE_IMAGE_PATH)

        # Dict page -> image
        self.page_image_dict = {
            UI.START_PAGE: self.start_image,
            UI.LAYOUT_PAGE: self.layout_image,
            UI.IN_GAME_PAGE: self.in_game_image,
            UI.MENU_BAR_PAGE: self.menu_bar_image,
            UI.VICTORY_PAGE: self.victory_image,
            UI.LOST_PAGE: self.lost_image
        } 


    def set_up_window(self):
        """Set up the Pygame window and return the screen object."""
        self.screen = pygame.display.set_mode((1200, 700))  # Set the screen size to 1200x700
        pygame.display.set_caption("Plants vs Zombies")  # Set the window caption
        self.__initialization()
        self.current_page = UI.START_PAGE
        return self.screen

    def draw_timer(self):
        """Draw the timer in the upper right corner of the screen."""
        font = pygame.font.Font(None, 50)  # Use a built-in font with size 36
        current_time = self.time.get_current_time()
        minutes = current_time // 60
        seconds = current_time % 60
        time_str = f"{minutes:02}:{seconds:02}"  # Format as mm:ss
        text_surface = font.render(time_str, True, (0, 0, 0))  # White color text
        text_rect = ((UI.IN_GAME_PAGE_TIMER_BAR["x_left_pos"] + UI.IN_GAME_PAGE_TIMER_BAR["x_right_pos"]) // 2 - 20, (UI.IN_GAME_PAGE_TIMER_BAR["y_up_pos"] + UI.IN_GAME_PAGE_TIMER_BAR["y_down_pos"]) // 2 - 13) 
        self.screen.blit(text_surface, text_rect)  # Draw in upper right

    def draw_sun_bar(self, current_sun):
        # # Calculate the current time in mm:ss format
        # total_seconds = time_obj.get_current_time()
        # minutes = total_seconds // 60
        # seconds = total_seconds % 60
        # time_string = f"{minutes:02}:{seconds:02}"

        # # Position the timer box using the provided coordinates
        # box_x = self.x_left_pos
        # box_y = self.y_up_pos

        # # Draw the white rectangle for the timer box
        # timer_rect = pygame.Rect(box_x, box_y, self.TIMER_BAR_WIDTH, self.TIMER_BAR_HEIGHT)
        # pygame.draw.rect(self.screen, (255, 255, 255), timer_rect)

        # # Render the timer text
        # text_surface = self.font.render(time_string, True, (0, 0, 0))  # Black text
        # text_rect = text_surface.get_rect(center=timer_rect.center)



        """Draw the sun-bar in the upper letf corner of the screen."""
        font = pygame.font.Font(None, 50)  # Use a built-in font with size 36
        sun_str = f"{current_sun}"  # Format normally
        text_surface = font.render(sun_str, True, (0, 0, 0))  # White color text

        text_rect = ((UI.IN_GAME_PAGE_SUN_BAR["x_left_pos"] + UI.IN_GAME_PAGE_SUN_BAR["x_right_pos"]) // 2 - 11, (UI.IN_GAME_PAGE_SUN_BAR["y_up_pos"] + UI.IN_GAME_PAGE_SUN_BAR["y_down_pos"]) // 2 - 13) 
        self.screen.blit(text_surface, text_rect)  # Draw in upper right

    def apply_blur(self, surface, scale_factor=0.1):
        """Apply a simple blur effect by scaling down and back up."""
        small_surface = pygame.transform.smoothscale(surface, (int(surface.get_width() * scale_factor), int(surface.get_height() * scale_factor)))
        blurred_surface = pygame.transform.smoothscale(small_surface, surface.get_size())
        return blurred_surface

    def draw_start_page(self):
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

    def draw_victory_page(self):
        """Draw the won page background."""
        image_rect = self.victory_image.get_rect()
        x_position = (self.screen.get_width() - image_rect.width) // 2  # Center horizontally
        y_position = (self.screen.get_height() - image_rect.height) // 2  # Center vertically

        self.screen.blit(self.victory_image, x_position, y_position)
        self.current_page = self.VICTORY_PAGE

    def draw_lost_page(self):
        """Draw the won page background."""
        image_rect = self.lost_image.get_rect()
        x_position = (self.screen.get_width() - image_rect.width) // 2  # Center horizontally
        y_position = (self.screen.get_height() - image_rect.height) // 2  # Center vertically

        self.screen.blit(self.lost_image, x_position, y_position)
        self.current_page = self.LOST_PAGE

    def draw_end_game_text(self):
        # Set up text
        white = (255, 255, 255)
        text = pygame.font.render("Press any key to Exit", True, white)
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 50))
        self.screen.blit(text, text_rect)

    def draw_menu_bar_page(self):
        """Draw the menu bar image on top of the current background without scaling."""
        background_image = self.page_image_dict[self.prev_page]
        background_image = self.apply_blur(background_image)

        image_rect = self.menu_bar_image.get_rect()

        x_position = (self.screen.get_width() - image_rect.width) // 2  # Center horizontally
        y_position = (self.screen.get_height() - image_rect.height) // 2  # Center vertically

        self.screen.blit(background_image, (0, 0))
        self.screen.blit(self.menu_bar_image, (x_position, y_position))
        self.current_page = self.MENU_BAR_PAGE

    def draw_given_image(self, image, x_pos, y_pos):  # (x, y) are the center posiotn of image
        self.screen.blit(image, (x_pos - image.get_width() // 2, y_pos - image.get_height() // 2))

    def draw_portable_image(self, image, x_pos_mouse, y_pos_mouse):
        if image is not None:
            self.screen.blit(image, (x_pos_mouse - int((3 / 4) * image.get_rect().width), y_pos_mouse - int((3 / 4) * image.get_rect().height)))

    def get_current_page(self):
        return self.current_page
    
    def set_current_page(self, page):
        self.current_page = page

    def get_prev_page(self):
        return self.prev_page
    
    def set_prev_page(self, page):
        self.prev_page = page

    def draw_object(self, image, x_pos, y_pos):  # x_pos and y_pos are the left-upper corner of the image
        self.screen.blit(image, (x_pos, y_pos))

    def clear_screen(self):
        white = (255,255,255)
        black = (0, 0, 0)
        self.screen.fill(black)

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
