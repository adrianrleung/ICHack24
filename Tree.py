import json

from Chapter import Chapter

CHAPTER_1 = "chapter_1.json"

class Tree:
    def __init__(self):
        self.root = Chapter(CHAPTER_1)