import Tree

# class textBlock:
#     def __init__(self, text):
#         self.text = text

# class Decision:
#     def __init__(self, text)

class Level:
    def __init__(self, filename):
        data = self.importJSON(filename)
        self.data = data
        self.choices = data["choices"]
        self.correct = data["correct"]
        self.description = data["description"]

    
    def launchLevel(self):
        for line in self.description:
            print("System: " + line)
        print("Your choices: ")
        for choice in self.choices:
            print(choice)
        userChoice = input("enter your choice")
        while userChoice > len(self.choices) or userChoice < 0:
            userChoice = input("invalid. Try again")
        if userChoice == self.correct:
            return True
        else:
            return False
        
    def importJSON(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data
    