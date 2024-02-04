import json
import pygame
import os, sys
from Button import Button

CHOICES = "choices"
CORRECT = "correct"
DESCRIPTION = "description"

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

class Level:

    class GameState:

        def __init__(self, intro, correct, choices):
            self.state = "description"
            self.intro = intro
            self.choices = choices
            self.correct = correct
            self.playing = True
            self.lostlife = False
        
        def description(self):

            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            next_button = Button(WHITE, 'Next',(1000,700),50,'gradius')
            descriptions = []

            if type(self.intro) == str:
                self.intro = [self.intro]
            for text in self.intro:
                descriptions.append(Button(WHITE, 
                                    text,
                                    (100,350),30,'gradius'))
        
            
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
                        if len(descriptions) == 1:
                            self.state = "choice"
                            done = True
                        else:
                            descriptions.pop(0)
                        
            
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
                descriptions[0].draw(screen)
                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def choice(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            
            choice1 = Button(WHITE, "1. " + self.choices[0], (100,50),50,'gradius')
            choice2 = Button(WHITE, "2. " + self.choices[1], (100,250),50,'gradius')
            choice3 = Button(WHITE, "3. " + self.choices[2], (100,450),50,'gradius')
            choice4 = Button(WHITE, "4. " + self.choices[3], (100,650),50,'gradius')
            
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and choice1.colliding_with_mouse():
                        if 0 == self.correct:
                            self.state = "correct"
                        else:
                            self.state = "wrong"
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and choice2.colliding_with_mouse():
                        if 1 == self.correct:
                            self.state = "correct"
                        else:
                            self.state = "wrong"
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and choice3.colliding_with_mouse():
                        if 2 == self.correct:
                            self.state = "correct"
                        else:
                            self.state = "wrong"
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and choice4.colliding_with_mouse():
                        if 3 == self.correct:
                            self.state = "correct"
                        else:
                            self.state = "wrong"
                        done = True
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if choice1.colliding_with_mouse():
                    choice1.colour = GREY
                else:
                    choice1.colour = WHITE
                if choice2.colliding_with_mouse():
                    choice2.colour = GREY
                else:
                    choice2.colour = WHITE
                if choice3.colliding_with_mouse():
                    choice3.colour = GREY
                else:
                    choice3.colour = WHITE
                if choice4.colliding_with_mouse():
                    choice4.colour = GREY
                else:
                    choice4.colour = WHITE
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                choice1.draw(screen)
                choice2.draw(screen)
                choice3.draw(screen)
                choice4.draw(screen)
                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def correctAns(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            
            button = Button(WHITE, "Correct Answer!", (400,350),100,'gradius')
            next_button = Button(WHITE, "Next Level", (1000,700),50,'gradius')
            
            
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
                        done = True
                        self.lostlife = False
                        self.state = 'next'
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if next_button.colliding_with_mouse():
                    next_button.colour = GREY
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                next_button.draw(screen)
                button.draw(screen)
                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)
            
        def wrong(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            
            button = Button(WHITE, "Wrong Answer!", (100,100),100,'gradius')
            next_button = Button(WHITE, "Next Level", (1000,700),50,'gradius')
            
            
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
                        done = True
                        self.lostlife = True
                        self.state = 'next'
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if next_button.colliding_with_mouse():
                    next_button.colour = GREY
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                next_button.draw(screen)
                button.draw(screen)
                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def state_manager(self):
            if self.state == 'description':
                self.description()
            elif self.state == 'choice':
                self.choice()
            elif self.state == 'correct':
                self.correctAns()
            elif self.state == 'wrong':
                self.wrong()
            elif self.state == "next":
                self.playing = False


    def __init__(self, filename):
        self.data = self.importJSON(filename)
        self.choices = self.data[CHOICES]
        self.correct = self.data[CORRECT]
        self.description = self.data[DESCRIPTION]
        self.gameState = self.GameState(self.description, self.correct, self.choices)

    
    def launchLevel(self):
        # print("System: " + self.description)
        # print("Your choices: ")
        # for index,choice in enumerate(self.choices):
        #     print(str(index+1)+".",choice)
        # userChoice = input("enter your choice: ")
        # while not userChoice.isdigit() or int(userChoice) > len(self.choices) or int(userChoice) < 1:
        #     userChoice = print("Invalid. Try again")
        # userChoice = int(userChoice)-1 # Changes from 1 indexing to 0 indexing
        # return userChoice == self.correct
        self.gameState = self.GameState(self.description, self.correct, self.choices)
        while self.gameState.playing:
            self.gameState.state_manager()
        return not self.gameState.lostlife
        
    def importJSON(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data

# if __name__ == "__main__":
#     myLevel = Level("Chapters/chapter_1/Levels/level_01.json")
#     myLevel.launchLevel()
    