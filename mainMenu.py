from Chapter import Chapter
import os, sys
import pygame
import pygame_menu
from Button import Button
# Main menu (tree of connected chapter)
# Variables
#   Hearts variable for lives remaining
# Functions

#keeps track of all nodes accessible

MAX_LIVES = 3

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0,255,255)
GREY = (100,100,100)

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class MainMenu:

    class GameState:

        def __init__(self, unlocked, lives):
            self.state = "selectChapter"
            self.unlocked = unlocked
            self.lives = lives
            self.playing = True
        
        def selectChapter(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            unlockedStrs = []
            for c in self.unlocked:
                unlockedStrs.append((str(c), c))
            menu = pygame_menu.Menu("menu", 700, 300)
            menu.add.selector(title = "Chapter", items = unlockedStrs, selector_id="Chapter", default = 0)
            next_button = Button(WHITE, "Next", (1000,700),50,'gradius')
            
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and next_button.colliding_with_mouse():
                        print("click")
                        currentChapter = menu.get_input_data()["Chapter"][0][1]
                        while self.lives != 0 and not currentChapter.complete:
                            for level in currentChapter.levels:
                                print(self.lives)
                                if not level.launchLevel():
                                    self.lives -= 1
                                if self.lives == 0:
                                    break
                            if self.lives != 0:
                                currentChapter.complete = True
                                print("current chapter complete")
                        if self.lives <= 0:
                            print("gameOver")
                            self.state = "gameOver"
                            for level in currentChapter.levels:
                                level.gameState.playing = True
                        else:
                            currentChapter.complete = False
                            for level in currentChapter.levels:
                                level.gameState.playing = True
                                level.gameState.lostlife = False
                            for child in currentChapter.children:
                                self.unlocked.append(child)
                                print("unlocked " + str(child))
                        done = True
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if next_button.colliding_with_mouse():
                    next_button.colour = GREY
                else:
                    next_button.colour = WHITE
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                next_button.draw(screen)
                if menu.is_enabled():
                    menu.update(pygame.event.get())
                    menu.draw(screen)

                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def gameOver(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            
            text = Button(WHITE, "Reset?", (500,200),50,'gradius')
            yes = Button(WHITE, "YES", (100, 600), 50,  "")
            no = Button(WHITE, "NO", (1000, 600), 50, "")
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and yes.colliding_with_mouse():
                        self.state = "selectChapter"
                        self.lives = MAX_LIVES
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and no.colliding_with_mouse():
                        done = True
                        self.playing = False

                    
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if yes.colliding_with_mouse():
                    yes.colour = GREY
                else:
                    yes.colour = WHITE
                if no.colliding_with_mouse():
                    no.colour = GREY
                else:
                    no.colour = WHITE
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                yes.draw(screen)
                no.draw(screen)
                text.draw(screen)

                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)
        
        def state_manager(self):
            if self.state == "selectChapter":
                self.selectChapter()
            if self.state == "gameOver":
                self.gameOver()

    def __init__(self, lives):
        self.unlocked = [Chapter.initChapter()]
        self.rest = []
        self.gameState = self.GameState(self.unlocked, lives)


def main():
    # reset = 1
    # mainMenu = MainMenu(MAX_LIVES)

    # path = "./Chapters"
    # chapters = os.listdir( path )

    # for chapter in chapters:
    #     for file in chapter:
    #         if os.path.isfile(file):
    #             mainMenu.rest.append(Chapter(file))


    # while reset != 0:
    #     stop = False
    #     print("Lives: " + str(mainMenu.lives))
    #     print("Current unlocked Chapters: ")
    #     for index,chapter in enumerate(mainMenu.unlocked):
    #         print(str(index+1)+".", chapter)
    #     userChoice = input("enter your choice of chapter: ")
    #     while not userChoice.isdigit() or int(userChoice) < 1 or int(userChoice) > len(mainMenu.unlocked):
    #         print("Invalid. Try again")
    #         userChoice = input("enter your choice of chapter: ")
    #     userChoice = int(userChoice) - 1

    #     currentChapter = mainMenu.unlocked[userChoice]
    #     while not stop:
    #         while mainMenu.lives != 0 and not currentChapter.complete:
    #             for level in currentChapter.levels:
    #                 if mainMenu.lives == 0:
    #                     break
    #                 if not level.launchLevel():
    #                     print("Wrong answer! lives - 1")
    #                     mainMenu.lives -= 1
    #             if mainMenu.lives != 0:
    #                 currentChapter.complete = True
    #         if mainMenu.lives == 0:
    #             print("You ran out of lives!")
    #             reset = input("reset chapter?: 0 (no) / 1 (yes)")
    #             while not reset.isdigit() or int(reset) not in [0,1]:
    #                 userChoice = input("Invalid. Try again")
    #             reset = int(reset)
    #             if reset == 0:
    #                 stop = True
    #             else:
    #                 currentChapter.reset()
    #                 mainMenu.lives = MAX_LIVES
    #         else:
    #             for child in currentChapter.children:
    #                 mainMenu.unlocked.append(child)
    #             stop = True
    mainMenu = MainMenu(MAX_LIVES)
    while mainMenu.gameState.playing:
        mainMenu.gameState.state_manager()



if __name__ == "__main__":
    main()



        



    







    



