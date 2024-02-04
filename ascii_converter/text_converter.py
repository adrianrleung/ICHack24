import pyfiglet
from ascii_magic import AsciiArt
class text_converter():
    def __init__(self) -> None:
        my_art = AsciiArt.from_image('img\eye.png')
        my_art.to_terminal(columns=80)
        self.text = input("please input the text you want to transfer: ")
    def render(self):
        print(pyfiglet.figlet_format(self.text, font="weird"))
