from Chapter import Chapter
from Tree import Tree
# Main menu (tree of connected chapter)
# Variables
#   Hearts variable for lives remaining
# Functions

#keeps track of all nodes accessible
class MainMenu:
    def __init__(self, lives):
        self.lives = lives
        self.root = Chapter("chapter_1.json")
        self.unlocked = [self.root]
        self.tree = Tree(self.root, self.unlocked)

        



    







    



