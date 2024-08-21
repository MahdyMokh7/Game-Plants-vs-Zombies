import os
import pygame
import sys
from UI import UI

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Define the rectangle position using a dictionary
rectangle_position = {
    "x_left_pos": 458,
    "y_up_pos": 398,
    "x_right_pos": 738,
    "y_down_pos": 485
}

def is_mouse_within_rectangle(mouse_pos, rect_pos):
    """Check if the mouse is within the rectangle defined by rect_pos."""
    return rect_pos["x_left_pos"] <= mouse_pos[0] <= rect_pos["x_right_pos"] and \
           rect_pos["y_up_pos"] <= mouse_pos[1] <= rect_pos["y_down_pos"]

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display without the resizable flag
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1200x700 Window with Background Image")

    # Use os.path.join to create the correct path from UI class
    image_path = UI.START_PAGE_IMAGE_PATH

    # Load the background image
    background_image = pygame.image.load(image_path)

    # Scale the image to fit the screen size
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                if is_mouse_within_rectangle(mouse_pos, rectangle_position):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if is_mouse_within_rectangle(mouse_pos, rectangle_position):
                        print("Clicked inside the rectangle")

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if is_mouse_within_rectangle(mouse_pos, rectangle_position):
                        print("yes")

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
