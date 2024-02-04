from PIL import Image
from ascii_magic import AsciiArt,Back
from tkinter  import Tk, Label
import tkinter  as tk
import cv2
import subprocess
import shlex

id_cmd='xdotool getactivewindow'
resize_cmd='xdotool windowsize --usehints {id} 100 30'

proc=subprocess.Popen(shlex.split(id_cmd),stdout=subprocess.PIPE)
windowid,err=proc.communicate()
proc=subprocess.Popen(shlex.split(resize_cmd.format(id=windowid)))
proc.communicate()

vid = cv2.VideoCapture("./out.mp4")


class ascii_renderer():
    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
        my_art = AsciiArt.from_image('img\mouth_open.jpg')
        my_art.to_terminal(columns=80)

    def push(self) :
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            my_art = AsciiArt.from_pillow_image(Image.fromarray(frame))
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            print(my_art.to_terminal(columns=120,back=Back.RED))
            # cv2.imshow('frame', gray)
            if cv2.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

# master = tk.Tk()

# def create_window(): #Definion und Festlegung neues Fenster
#     toplevel = Toplevel()
#     toplevel.title('result')
#     toplevel.geometry('1500x1000')
#     toplevel.focus_set()

# Button(master, command=create_window).pack(padx=5, anchor=N, pady=4)

# master.mainloop()
'''
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

class image_to_ascii():
    def __init__(self,path) -> None:
        try:
            self.image = PIL.Image.open(path)
        except:
            print(path, "Unable to find image ")
        self.imagePath = path
    def resize(self, new_width = 100):
        width, height = self.image.size
        new_height = int(new_width * height / width)
        print(self.image.size)
        self.image = self.image.resize((new_width, new_height))
    def to_greyscale(self):
        self.image = self.image.convert("L")
    def pixel_to_ascii(self) -> str:
        pixels = self.image.getdata()
        ascii_str = ""
        for pixel in pixels:
            ascii_str += ASCII_CHARS[pixel//25]
        return ascii_str
    def to_ascii(self):
        self.resize()
        self.to_greyscale()
        return self.pixel_to_ascii()

'''    

def main():
    my_renderer = ascii_renderer()
    my_renderer.push()
main()
