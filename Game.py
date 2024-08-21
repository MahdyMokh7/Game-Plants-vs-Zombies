import pygame
from Time import Time
from UI import UI
from Map import Map
from AudioManager import AudioManager


class Game:
    def __init__(self):
        self.running = False
        self.users = []  
        self.bots = []     
        self.time = Time() 
        self.maap = Map()
        self.ui = UI(time=self.time, maap=self.maap)   
        self.audioManager = AudioManager()

    def handle_events(self):
        """Handle game events."""
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False  # Handle quit event
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.iconify()  # Minimize window when ESC is pressed
                
            elif event.type == pygame.WINDOWMINIMIZED:
                print("Window minimized")  # Handle window minimize event
                
            elif event.type == pygame.WINDOWRESTORED:
                print("Window restored")  # Handle window restore event

            else:
                self.run_page(event)

    @staticmethod
    def is_mouse_within_rectangle(mouse_pos, rect_pos):
        """Check if the mouse is within the rectangle defined by rect_pos."""
        return rect_pos["x_left_pos"] <= mouse_pos[0] <= rect_pos["x_right_pos"] and \
            rect_pos["y_up_pos"] <= mouse_pos[1] <= rect_pos["y_down_pos"]

    def run_start_page(self, event):
        self.ui.draw_start_page()
        self.audioManager.play_music(AudioManager.DEFEAT)
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if Game.is_mouse_within_rectangle(mouse_pos, UI.START_PAGE_START_BAR_RECTANGLE_POSITION):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangle(mouse_pos, UI.START_PAGE_START_BAR_RECTANGLE_POSITION):
                    print("Clicked inside the rectangle")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangle(mouse_pos, UI.START_PAGE_START_BAR_RECTANGLE_POSITION):
                    self.ui.set_current_page(UI.LAYOUT_PAGE)
                    print("yes")

    def run_layout_page(self, event):
        return "Function Two executed!"

    def run_in_game(self, event):
        return "Function Three executed!"

    def run_page(self, event):
        option = self.ui.get_current_page()
        switcher = {
            UI.START_PAGE: self.run_start_page,
            UI.LAYOUT_PAGE: self.run_layout_page,
            UI.IN_GAME_PAGE: self.run_in_game
        }
        func = switcher.get(option, lambda: "ERROR: Invalid option to run page")
        return func(event)

    def run(self):
        pygame.init()

        screen = self.ui.set_up_window()

        # Main Loop
        self.running = True
        clock = pygame.time.Clock()  # Initialize the clock for framerate control
        state = self.ui.get_current_page()  # Initial state to start with the start page
        while self.running:
            self.handle_events()

            clock.tick(60)  # 60FPS
            pygame.display.flip()  # Update screen

        pygame.quit()


    def initialization(self):
        """Initialize time and map."""
        pass


if __name__ == "__main__":
    game = Game()
    game.run()