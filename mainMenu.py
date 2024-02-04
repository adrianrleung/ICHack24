from Chapter import Chapter
import os, sys
# Main menu (tree of connected chapter)
# Variables
#   Hearts variable for lives remaining
# Functions

#keeps track of all nodes accessible

MAX_LIVES = 3

class MainMenu:
    def __init__(self, lives):
        self.lives = lives
        self.unlocked = [Chapter.initChapter()]
        self.rest = []


def main():
    mainMenu = MainMenu(MAX_LIVES)

    path = "./Chapters"
    chapters = os.listdir( path )

    for chapter in chapters:
        for file in chapter:
            if os.path.isfile(file):
                mainMenu.rest.append(Chapter(file))


    while True:
        stop = False
        print("Lives: " + str(mainMenu.lives))
        print("Current unlocked Chapters: ")
        for index,chapter in enumerate(mainMenu.unlocked):
            print(str(index+1)+".", chapter)
        userChoice = input("enter your choice of chapter: ")
        while userChoice > len(mainMenu.unlocked) or userChoice < 1 or not userChoice.isdigit():
            print("Invalid. Try again")
            userChoice = input("enter your choice of chapter: ")
        userChoice = int(userChoice) - 1

        currentChapter = mainMenu.unlocked[userChoice]
        while not stop:
            while mainMenu.lives != 0 and not currentChapter.complete:
                for level in currentChapter.children:
                    if mainMenu.lives == 0:
                        break
                    level.launchLevel()
                currentChapter.complete = True
            if mainMenu.lives == 0:
                reset = input("reset chapter?: 0 (no) / 1 (yes)")
                while not reset.isdigit() or reset not in [0,1]:
                    userChoice = input("Invalid. Try again")
                if reset == 0:
                    stop = True
                else:
                    currentChapter.reset()
                    mainMenu.lives = MAX_LIVES
            else:
                for child in currentChapter.children:
                    mainMenu.unlocked.append(child)
                stop = True



if __name__ == "__main__":
    main()



        



    







    



