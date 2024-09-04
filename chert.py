
        # Load your custom font  
        font_path = "OpenSans-Semibold.ttf"  # Replace with the name of your downloaded font file  
        font_size = 33
        font = pygame.font.Font(font_path, font_size)  # Use your custom font  

        # Format the number to be displayed  
        sun_str = f"{current_sun:,}"  # Format with commas as a thousands separator  
        text_surface = font.render(sun_str, True, (0, 0, 0))  # Black color text  

        # Calculate the position to display the text  
        text_rect = (  
            (UI.IN_GAME_PAGE_SUN_BAR["x_left_pos"] + UI.IN_GAME_PAGE_SUN_BAR["x_right_pos"]) / 2 - 13,  
            (UI.IN_GAME_PAGE_SUN_BAR["y_up_pos"] + UI.IN_GAME_PAGE_SUN_BAR["y_down_pos"]) / 2 - 23  
        )  

        # Draw the text on the screen  
        self.screen.blit(text_surface, text_rect)  # Draw in the specified position   

        # Don't forget to update the display after blitting  
        pygame.display.flip()