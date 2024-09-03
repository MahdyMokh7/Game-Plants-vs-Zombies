import pygame  
import sys  

# Initialize Pygame  
pygame.init()  

# Set up the display  
width, height = 700, 700  
window = pygame.display.set_mode((width, height))  
pygame.display.set_caption("Rectangle in Center")  

# Define colors  
background_color = (255, 255, 255)  # White  
rectangle_color = (255, 0, 0)  # Red  

# Rectangle properties  
rectangle_width = 50  
rectangle_height = 100  
rectangle_position = (width // 2 - rectangle_width // 2, height // 2 - rectangle_height // 2)  # Center of the window  

# Main loop  
while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()  

    # Fill the background  
    window.fill(background_color)  

    # Draw the rectangle  
    pygame.draw.rect(window, rectangle_color, (rectangle_position[0], rectangle_position[1], rectangle_width, rectangle_height))  

    # Update the display  
    pygame.display.flip()