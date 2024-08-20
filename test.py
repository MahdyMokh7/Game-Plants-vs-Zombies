import os
import pygame
import sys

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display without the resizable flag
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

            # Handle mouse movement (hover) - just pass
            elif event.type == pygame.MOUSEMOTION:
                pass

            # Handle mouse click to print the position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(f"Mouse clicked at position: {mouse_pos}")

            # Handle the Esc key to minimize the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
