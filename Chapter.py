import json

from Level import Level

CHAPTER_1 = "chapter_1.json"
LEVELS = "levels"
DEPENDENCIES = "dependencies"

class Chapter:
    def __init__(self, filename):
        dict = self.importJSON(filename)

        self.index = 0
        self.complete = False
        self.levels = []
        self.children = []

        for level_json in dict[LEVELS]:
            self.levels.append(Level(level_json))

        for chapter_json in dict[DEPENDENCIES]:
            chapter = Chapter(chapter_json)
            self.children.append(chapter)

    def reset(self):
        self.index = 0

    @staticmethod
    def initChapter():
        return Chapter(CHAPTER_1)

    def importJSON(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data

