from Chapter import Chapter
import os, sys
import pygame
import pygame_menu
from Button import Button
import sqlite3
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

def nextIndex():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("Select UserID from Users")
    UserIDs = cur.fetchall()
    for i in range(len(UserIDs)):
        UserIDs[i] = UserIDs[i][0]
    count = 0
    while count in UserIDs:
        count += 1
    return count

Cs = ["Chapters/chapter_2/chapter_2.json",
      "Chapters/chapter_3/chapter_3.json",
      "Chapters/chapter_4/chapter_4.json",
      "Chapters/chapter_5/chapter_5.json"]

class MainMenu:

    class GameState:

        def __init__(self, unlocked, lives):
            self.state = "login"
            self.unlocked = unlocked
            self.lives = lives
            self.playing = True
            self.currID = None
        
        def updateTable(self):
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cmd = "SELECT * from CompletedChapters WHERE UserID = ?"
            data = [self.currID]
            cur.execute(cmd, data)
            for i in range(len(cur.fetchall())+1, len(self.unlocked)+1):
                cmd = '''INSERT INTO CompletedChapters(
                                        UserID, Chapter) VALUES 
                                        (?, ?)'''
                data = [self.currID, i]
                cur.execute(cmd, data)
            conn.commit()
            conn.close()
            
        

        def login(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
        
            menu = pygame_menu.Menu("menu", 700, 300)
            menu.add.text_input('Username: ', default='', textinput_id="username")
            menu.add.text_input('Password: ', default='', password=True, textinput_id="password")
            next_button = Button(WHITE, "Next", (1000,700),50)
            signup_button = Button(WHITE, "Make account", (100, 700), 50)
            text = Button(WHITE, "Login", (400, 100), 50)
            
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and next_button.colliding_with_mouse():
                        items = menu.get_input_data()
                        username = items["username"]
                        password = items["password"]
                        
                        conn = sqlite3.connect('database.db')
                        cur = conn.cursor()
                        cmd = "SELECT UserID from USERS WHERE Username = ? AND Password = ?"
                        data = [username, password]

                        cur.execute(cmd, data)
                        id = cur.fetchone()
                        if id == None:
                            print("invalid login")
                        else:
                            cmd = "SELECT * from CompletedChapters WHERE UserID = ?"
                            self.currID = id[0]
                            data = [self.currID]
                            cur.execute(cmd, data)
                            chaptersToLoad = 0
                            d = cur.fetchall()
                            if d != None:
                                chaptersToLoad = len(d) - 1
                            for i in range(chaptersToLoad):
                                self.unlocked.append(Chapter(Cs[i]))
                            self.state = "selectChapter"
                            done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and signup_button.colliding_with_mouse():
                        self.state = "signup"
                        done = True
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if next_button.colliding_with_mouse():
                    next_button.colour = GREY
                else:
                    next_button.colour = WHITE
                if signup_button.colliding_with_mouse():
                    signup_button.colour = GREY
                else:
                    signup_button.colour = WHITE
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                next_button.draw(screen)
                signup_button.draw(screen)
                text.draw(screen)
                if menu.is_enabled():
                    menu.update(events)
                    menu.draw(screen)

                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def signup(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
        
            menu = pygame_menu.Menu("menu", 700, 300)
            menu.add.text_input('Username: ', default='', textinput_id="username")
            menu.add.text_input('Password: ', default='', password=True, textinput_id="password")
            next_button = Button(WHITE, "Next", (1000,700),50)
            login_button = Button(WHITE, "Go to login", (100, 700), 50)
            text = Button(WHITE, "Sign Up", (400, 100), 50)
            
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and next_button.colliding_with_mouse():
                        self.state = "login"
                        items = menu.get_input_data()
                        username = items["username"]
                        password = items["password"]
                        nextID = nextIndex()
                        print(nextID)
                        conn = sqlite3.connect('database.db')
                        cur = conn.cursor()
                        cmd = '''INSERT INTO USERS(
                                        UserID, Username, Password) VALUES 
                                        (?, ?, ?)'''
                        data = [nextID, username, password]
                        cur.execute(cmd, data)
                        conn.commit()
                        conn.close()
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN and login_button.colliding_with_mouse():
                        self.state = "login"
                        done = True
                        
            
                # --- Game logic should go here
                
                #Check if mouse is over campaign button
                
                #Check if mouse is over back button
                if next_button.colliding_with_mouse():
                    next_button.colour = GREY
                else:
                    next_button.colour = WHITE
                if login_button.colliding_with_mouse():
                    login_button.colour = GREY
                else:
                    login_button.colour = WHITE
                # --- Screen-clearing code goes here
                screen.fill(BLACK)
            
                # --- Drawing code should go here
                
                #Blitting the text for the buttons on the screen
                next_button.draw(screen)
                login_button.draw(screen)
                text.draw(screen)
                if menu.is_enabled():
                    menu.update(events)
                    menu.draw(screen)

                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def selectChapter(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            unlockedStrs = []
            for c in self.unlocked:
                unlockedStrs.append((str(c), c))
            menu = pygame_menu.Menu("menu", 700, 300)
            menu.add.selector(title = "Chapter", items = unlockedStrs, selector_id="Chapter", default = 0)
            next_button = Button(WHITE, "Next", (1000,700),50)
            
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Check for a mouse click and if the coordinates of the mouse are also over the play button, the screen is set to the main game
                    if event.type == pygame.MOUSEBUTTONDOWN and next_button.colliding_with_mouse():
                        currentChapter = menu.get_input_data()["Chapter"][0][1]
                        while self.lives != 0 and not currentChapter.complete:
                            for level in currentChapter.levels:
                                if not level.launchLevel():
                                    self.lives -= 1
                                if self.lives == 0:
                                    break
                            if self.lives != 0:
                                currentChapter.complete = True
                                self.updateTable()
                        if self.lives <= 0:
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
                    menu.update(events)
                    menu.draw(screen)

                
                #Update display
                pygame.display.flip()
            
                #Make the game run at 60 frames per second
                clock.tick(60)

        def gameOver(self):
            pygame.display.set_caption('Level')

             # Loop until the user clicks the close button.
            done = False
            
            
            text = Button(WHITE, "Reset?", (500,200),50)
            yes = Button(WHITE, "YES", (100, 600), 50)
            no = Button(WHITE, "NO", (1000, 600), 50)
            
            # -------- Main Program Loop -----------
            while not done:
                # --- Main event loop
                
                #Get the mouse coordinates
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.updateTable()
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
            if self.state == "login":
                self.login()
            if self.state == "signup":
                self.signup()

    def __init__(self, lives):
        self.unlocked = [Chapter.initChapter()]
        self.rest = []
        self.gameState = self.GameState(self.unlocked, lives)