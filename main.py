from mainMenu import MainMenu
MAX_LIVES = 3

def main():
    mainMenu = MainMenu(MAX_LIVES)
    while mainMenu.gameState.playing:
        mainMenu.gameState.state_manager()



if __name__ == "__main__":
    main()