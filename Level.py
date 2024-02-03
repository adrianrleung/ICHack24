import Tree

# class textBlock:
#     def __init__(self, text):
#         self.text = text

# class Decision:
#     def __init__(self, text)

class Level:
    def __init__(self, data):
        self.data = data

    
    def launchLevel(self):
        for line in data[description]:
            print("System " + text)
        for choice in data[choices]:
            userChoice = input(choice)
            while userChoice.upper() not in ["Y","N"]:
                userChoice = input("invalid input, try again")
            if userChoice != data[correct]:
                self.fail()
            else:
                self.corrects.pop(0)
        self.right()
    
    def fail(self):
        pass

    def right(self):
        pass