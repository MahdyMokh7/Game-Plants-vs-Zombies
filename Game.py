import pygame
import sys
from Time import Time
from UI import UI
from Map import Map
from AudioManager import AudioManager
from Bot import Bot
from Plant import *


class Game:
    def __init__(self):
        self.running = False
        # self.users = []  
        # self.bots = []     
        self.time = Time() 
        self.maap = Map()
        self.ui = UI(time=self.time, maap=self.maap)   
        self.audioManager = AudioManager()
        self.bot = Bot(time=self.time, maap=self.maap)

        self.is_picture_on_hold = False  # picture is on hold but hasnt yet be planted
        self.selected_plant_type = None  # the picture (plant type) on hold 

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
    def is_mouse_within_rectangles(mouse_pos, *rect_positions):
        """Check if the mouse is within any of the rectangles defined by rect_positions."""
        for rect_pos in rect_positions:
            if (rect_pos["x_left_pos"] <= mouse_pos[0] <= rect_pos["x_right_pos"] and
                    rect_pos["y_up_pos"] <= mouse_pos[1] <= rect_pos["y_down_pos"]):
                return True
        return False

    def run_start_page(self, event):
        self.ui.draw_start_page()
        # self.audioManager.play_music(AudioManager.DEFEAT)
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if Game.is_mouse_within_rectangles(mouse_pos, UI.START_PAGE_START_BAR_RECTANGLE_POSITION):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:   ### delete
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangles(mouse_pos, UI.START_PAGE_START_BAR_RECTANGLE_POSITION):
                    self.ui.set_current_page(UI.LAYOUT_PAGE)
                    self.ui.set_prev_page(UI.START_PAGE)
                    print("Clicked inside the rectangle")

        if event.type == pygame.MOUSEBUTTONUP:  
            if event.button == 1:  # Left click
                mouse_pos = event.pos


    def run_layout_page(self, event):
        self.ui.draw_layout_page()
        self.audioManager.play_music(AudioManager.LAYOUT_PAGE_MUSIC)

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if Game.is_mouse_within_rectangles(mouse_pos, UI.LAYOUT_PAGE_ADVENTURE_BAR_RECTANGLE_POSITION, 
                                              UI.LAYOUT_PAGE_OPTIONS_BAR_RECTANGLE_POSITION, 
                                              UI.LAYOUT_PAGE_QUIT_BAR_RECTANGLE_POSITION):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangles(mouse_pos, UI.LAYOUT_PAGE_ADVENTURE_BAR_RECTANGLE_POSITION):  # adventure
                    self.ui.set_current_page(UI.IN_GAME_PAGE)
                    self.ui.set_prev_page(UI.LAYOUT_PAGE)
                    self.audioManager.stop_music()
                    print("adventure")

                elif Game.is_mouse_within_rectangles(mouse_pos, UI.LAYOUT_PAGE_OPTIONS_BAR_RECTANGLE_POSITION):  # options
                    self.ui.set_current_page(UI.MENU_BAR_PAGE)
                    self.ui.set_prev_page(UI.LAYOUT_PAGE)
                    print("options")

                elif Game.is_mouse_within_rectangles(mouse_pos, UI.LAYOUT_PAGE_QUIT_BAR_RECTANGLE_POSITION):  # quit
                    self.running = False  ### pygame.quit()
                    print("quit")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click
                mouse_pos = event.pos


    def run_menu_page(self, event):
        self.ui.draw_menu_bar_page()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if Game.is_mouse_within_rectangles(mouse_pos, UI.MENU_PAGE_CONTINUE_BAR_RECTABGLE_POSITION, 
                                              UI.MENU_PAGE_SPEED_BAR_RECTABGLE_POSITION, 
                                              UI.MENU_PAGE_MUTE_BAR_RECTABGLE_POSITION):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangles(mouse_pos, UI.MENU_PAGE_CONTINUE_BAR_RECTABGLE_POSITION):  # continue
                    self.ui.set_current_page(self.ui.prev_page)
                    print("continue")

                elif Game.is_mouse_within_rectangles(mouse_pos, UI.MENU_PAGE_SPEED_BAR_RECTABGLE_POSITION):  # speed
                    ############ change scale
                    print("speed")

                elif Game.is_mouse_within_rectangles(mouse_pos, UI.MENU_PAGE_MUTE_BAR_RECTABGLE_POSITION):  # mute-play sound
                    self.audioManager.play_pause_sound()
                    print("mute/play sound")


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                
    ###########################################333333333333333
    def run_in_game(self, event):
        self.ui.draw_in_game_page()
        self.audioManager.play_music(AudioManager.IN_GAME)


        if event.type == pygame.MOUSEMOTION:
            if not self.is_picture_on_hold:
                mouse_pos = event.pos
                if Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_MENU_BAR, 
                                                   UI.IN_GAME_PAGE_PEASHOOTER_BAR, 
                                                   UI.IN_GAME_PAGE_SIBZAMINI_BAR, 
                                                   UI.IN_GAME_PAGE_SNOWPEASHOOTER_BAR,
                                                   UI.IN_GAME_PAGE_SUNFLOWER_BAR):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            else:
                intended_image = Plant.get_image_by_type(self.selected_plant_type)
                self.ui.draw_portable_image(intended_image, mouse_pos.x, mouse_pos.y)

        if event.type == pygame.MOUSEBUTTONDOWN:    # ###################

            if not self.is_picture_on_hold:
                if event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_MENU_BAR):  # menu-bar
                        self.ui.set_current_page(UI.MENU_BAR_PAGE)
                        self.ui.set_prev_page(UI.IN_GAME_PAGE)
                        # self.audioManager.stop_music()
                        print("menu-bar")

                    elif Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_PEASHOOTER_BAR):  # pea-shooter-select
                        if PeaShooter.is_available() and PeaShooter.is_sun_enough(self.user.get_nums_of_sun()):   # get gray when not available
                            self.is_picture_on_hold = True
                            self.selected_plant_type = PeaShooter.NAME
                            PeaShooter.last_time_selected = Time.get_global_time()
                            print("pea-shooter-select")

                    elif Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_SNOWPEASHOOTER_BAR):  # snowpeashooter-select
                        if SnowPeaShooter.is_available() and SnowPeaShooter.is_sun_enough(self.user.get_nums_of_sun()):
                            self.is_picture_on_hold = True
                            self.selected_plant_type = SnowPeaShooter.NAME
                            SnowPeaShooter.last_time_selected = Time.get_global_time()
                            print("snowpeashooter-select")
                        
                    elif Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_SUNFLOWER_BAR):  # sunflower-select
                        if Sunflower.is_available() and Sunflower.is_sun_enough(self.user.get_nums_of_sun()):
                            self.is_picture_on_hold = True
                            self.selected_plant_type = Sunflower.NAME
                            Sunflower.last_time_selected = Time.get_global_time()
                            print("sunflower-select")

                    elif Game.is_mouse_within_rectangles(mouse_pos, UI.IN_GAME_PAGE_SUNFLOWER_BAR):  # sibzamini-select
                        if Sibzamini.is_available()and Sibzamini.is_sun_enough(self.user.get_nums_of_sun()):
                            self.is_picture_on_hold = True
                            self.selected_plant_type = Sibzamini.NAME
                            Sibzamini.last_time_selected = Time.get_global_time()
                            print("sibzamini-select")

            else:
                if event.button == 1:  # Left click
                    mouse_pos = event.pos

                    if PeaShooter.NAME == self.selected_plant_type:   # get gray when not available  # pea-shooter-select
                        PeaShooter.last_time_selected = Time.get_global_time()       
                        self.user.dicrease_nums_of_sun(self , PEA_SHOOTER_PRICE)
                        print("peashooter-planted")

                    elif SnowPeaShooter.NAME == self.selected_plant_type:  # snowpeashooter-select
                        SnowPeaShooter.last_time_selected = Time.get_global_time()
                        self.user.dicrease_nums_of_sun(self , SNOW_PEA_SHOOTER_PRICE)
                        print("snowpeashooter-planted")
                    
                    elif Sunflower.NAME == self.selected_plant_type:  # sunflower-select
                        Sunflower.last_time_selected = Time.get_global_time()
                        self.user.dicrease_nums_of_sun(self , SUN_FLOWER_PRICE)
                        print("sunflower-planted")

                    elif Sibzamini.NAME == self.selected_plant_type:  # sibzamini-select
                        Sibzamini.last_time_selected = Time.get_global_time()
                        self.user.dicrease_nums_of_sun(self , SIB_ZAMINI_PRICE)
                        print("sibzamini-planted")

                    else:
                        print("ERROR: not a plant type got selected in the plant type select section!")
                        sys.exit()

                    self.user.place_the_plant(self.selected_plant_type, mouse_pos.x, mouse_pos.y)
                    self.is_picture_on_hold = True
                    self.selected_plant_type = None


        if event.type == pygame.MOUSEBUTTONUP:   
            if event.button == 1:  # Left click
                mouse_pos = event.pos
    

        status = self.bot.run()
        if status == Bot.WON_STATE:
            print("Victory")  # needs page dev. and work to do
            pygame.quit()
            sys.exit()
        elif status == Bot.LOST_STATE:
            print("Lost")  # needs page dev. and work to do  
            pygame.quit()
            sys.exit()
        else:
            pass
    ###################################################

    def run_page(self, event):
        option = self.ui.get_current_page()
        switcher = {
            UI.START_PAGE: self.run_start_page,
            UI.LAYOUT_PAGE: self.run_layout_page,
            UI.IN_GAME_PAGE: self.run_in_game,
            UI.MENU_BAR_PAGE: self.run_menu_page
        }
        func = switcher.get(option, lambda: "ERROR: Invalid option to run page")
        return func(event)

    def run(self):
        pygame.init()

        screen = self.ui.set_up_window()

        # Main Loop
        self.running = True
        clock = pygame.time.Clock()  # Initialize the clock for framerate control
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