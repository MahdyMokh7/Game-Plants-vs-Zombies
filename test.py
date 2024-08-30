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

def apply_blur(surface, scale_factor=0.4):
    """Apply a simple blur effect by scaling down and back up."""
    print(surface)
    small_surface = pygame.transform.smoothscale(surface, (int(surface.get_width() * scale_factor), int(surface.get_height() * scale_factor)))
    blurred_surface = pygame.transform.smoothscale(small_surface, surface.get_size())
    return blurred_surface

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display without the resizable flag
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1200x700 Window with Background Image")

    # Use os.path.join to create the correct path from UI class
    background_image_path = UI.IN_GAME_PAGE_IMAGE_PATH  
    image_path2 = UI.MENU_BAR_PAGE_IMAGE_PATH

    # Load the images
    background_image = pygame.image.load(background_image_path)
    foreground_image = pygame.image.load(image_path2)

    # Scale and blur the background image
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    blurred_background_image = apply_blur(background_image)

    # Get the rect of the foreground image for positioning
    image_rect = foreground_image.get_rect()
    x_position = (screen.get_width() - image_rect.width) // 2  # Center horizontally
    y_position = (screen.get_height() - image_rect.height) // 2  # Center vertically
    
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
                print(event.pos)
                if event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if is_mouse_within_rectangle(mouse_pos, rectangle_position):
                        print("Clicked inside the rectangle")

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if is_mouse_within_rectangle(mouse_pos, rectangle_position):
                        print("yes")

        # Draw the blurred background image
        screen.blit(blurred_background_image, (0, 0))

        # Draw the foreground image on top of the blurred background
        # screen.blit(foreground_image, (x_position, y_position))

        screen.blit(background_image, (0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()


def class_test():
    class a:
        def __init__(self):
            self.q = 10
            print("hi")
    class b:
        def __init__(self):
            self.q = 21
            print("hey")

    listt = [a, b]
    c = listt[1]()

def test2():
    class a:
        d = 10
    
    print(a.d)
    a.d = 20
    print(a.d)

if __name__ == "__main__":
    # main()
    # class_test()
    test2()
