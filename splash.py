from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Progressbar
# --------------------------
from home import Face_Recognition_system
from login import Login
import time
import os
import pyttsx3


class Splash:
    def mainWin(self):
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)

    def __init__(self, root):
        self.root = root
        self.root.title("FAMS - Initializing ...")
        self.root.geometry("500x500+350+100")

        # self.root.overrideredirect(1)

        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        background_img = Image.open("./img/Splash.png")
        background_img = background_img.resize(
            (500, 500), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(background_img)

        background_img = Label(self.root, image=self.photoimg1)
        background_img.place(x=0, y=0, width=500, height=500)

        self.engine.say('Initializing is in process, please wait')
        self.engine.runAndWait()


if __name__ == "__main__":
    root = Tk()
    root.resizable(0, 0)
    app = Splash(root)
    root.mainloop()
