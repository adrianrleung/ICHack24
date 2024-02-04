from PIL import Image
from ascii_magic import AsciiArt,Back
import cv2
import os 
from pick import pick
from pprint import pprint
import inquirer
import text_converter
import pyfiglet

class starter() :
    def __init__(self) -> None:
        my_art = AsciiArt.from_image('img\mouth_open.jpg')
        my_art.to_terminal(columns=80)
        print("Welcome to ASCII converter!!\n")
    def render(self):
        questions = [
        inquirer.List(
        "mode",
        message="What mode do you want to use?",
        choices=["text_converter", "video_render", "real-time_converter", "generativeAI_from_text", "tbc2", "tbc3"],
        ),
        ]
        answers = inquirer.prompt(questions)
        pprint(answers)
        return answers.get("mode")
        
class dalle_renderer():
    def __init__(self) -> None:
        my_art = AsciiArt.from_image('img\Brain.jpg')
        my_art.to_terminal(columns=100)
        self.text = input("please describe the ASCII art you want to generate: ")
        self.my_art = AsciiArt.from_craiyon(self.text,debug=True)
        
    def render(self):
        print(self.my_art.to_ascii(columns=200))
        
class ascii_renderer():
    def __init__(self,mode) -> None:
        dir_name = "vid/"
        vids = [ f for f in os.listdir(dir_name) if f.endswith('.avi') ]
        no_vids = len(vids)
        self.mode = mode
        if no_vids > 0 and mode == "video_render":
            print(dir_name+vids[0])
            print("detected" + str(no_vids) + "videos, trying to read the file")
            self.cap = cv2.VideoCapture(dir_name+vids[0])
        elif mode == "real-time_converter":
            print("no video detected")
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Cannot open camera")
                exit()
        elif mode == "generativeAI_from_text":
            self.cap = dalle_renderer()
        else :
            self.cap = text_converter.text_converter()
        
    def push(self) :
        print(self.mode)
        if self.mode == "generativeAI_from_text":
            self.cap.render()
        if self.mode == "text_converter":
            self.cap.render()
        else :
            while True:
                # Capture frame-by-frame
                ret, frame = self.cap.read()
                my_art = AsciiArt.from_pillow_image(Image.fromarray(frame))
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                print(my_art.to_terminal(columns=80))
                # cv2.imshow('frame', gray)
                if cv2.waitKey(1) == ord('q'):
                    break
            # When everything done, release the capture
            self.cap.release()
            cv2.destroyAllWindows()
    

def clean():
        if os.name == 'nt':
            _ = os.system('cls')
# def create_window(): #Definion und Festlegung neues Fenster
#     toplevel = Toplevel()
#     toplevel.title('result')
#     toplevel.geometry('1500x1000')
#     toplevel.focus_set()

# Button(master, command=create_window).pack(padx=5, anchor=N, pady=4)

# master.mainloop()


def main():
    flag = "Y"
    while flag == "Y":
        clean()
        start = starter()
        selection = start.render()
        clean()
        my_renderer = ascii_renderer(mode = selection)
        my_renderer.push()
        flag = input("Do you want to make another ASCII art? [Y/n]")
    print(pyfiglet.figlet_format("GoodBye", font="weird"))

main()
