import os
import pygame
import sys

# Constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 440

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display with resizable flag
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("1200x700 Window with Background Image")

    # Use os.path.join to create the correct path
    image_path = os.path.join("Image files", "background_image.png")

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

            # Handle window resize event
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # Scale the background image to the new window size
                background_image = pygame.transform.scale(background_image, (event.w, event.h))

            # Handle mouse movement
            elif event.type == pygame.MOUSEMOTION:
                # Get the mouse position
                mouse_pos = event.pos
                print(f"Mouse position: {mouse_pos}")

            # Handle maximize/minimize
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:  # Fullscreen toggle on F11
                    pygame.display.toggle_fullscreen()
                elif event.key == pygame.K_m:  # Minimize on 'M' key
                    pygame.display.iconify()

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
