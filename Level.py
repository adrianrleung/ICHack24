import json

CHOICES = "choices"
CORRECT = "correct"
DESCRIPTION = "description"

class Level:
    def __init__(self, filename):
        self.data = self.importJSON(filename)
        self.choices = self.data[CHOICES]
        self.correct = self.data[CORRECT]
        self.description = self.data[DESCRIPTION]

    
    def launchLevel(self):
        for line in self.description:
            print("System: " + line)
        print("Your choices: ")
        for index,choice in enumerate(self.choices):
            print(str(index+1)+".",choice)
        userChoice = input("enter your choice: ")
        while userChoice > len(self.choices) or userChoice > 1 or not userChoice.isdigit():
            userChoice = print("Invalid. Try again")
        userChoice = int(userChoice)-1 # Changes from 1 indexing to 0 indexing
        return userChoice == self.correct
        
    def importJSON(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data
    