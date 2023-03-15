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


splash_window = Tk()
splash_window.title("FAMS - Initializing ...")
splash_window.geometry("500x500+350+100")


background_img = Image.open("./img/Splash.png")
background_img = background_img.resize((500, 500), Image.Resampling.LANCZOS)
splash_window.photoimg1 = ImageTk.PhotoImage(background_img)

background_img = Label(splash_window, image=splash_window.photoimg1)
background_img.place(x=0, y=0, width=500, height=500)


splash_window.engine = pyttsx3.init('sapi5')
splash_window.voices = splash_window.engine.getProperty('voices')
splash_window.engine.setProperty('voice', splash_window.voices[0].id)

splash_window.engine.say('Initializing is in process, please wait')
splash_window.engine.runAndWait()


def mainWin(self):
    self.new_window = Toplevel(self.root)
    self.app = Login(self.new_window)


def Login_win():
    splash_window.destroy()

    Login_window = Tk()

    Login_window.title("Login")
    # Login_window = login_root
    # window.iconbitmap("logo.ico")
    Login_window.geometry("1280x700+0+0")

    Login_window.var_ssq = StringVar()
    Login_window.var_sa = StringVar()
    Login_window.var_pwd = StringVar()

    # Assistance Speak Variable
    Login_window.engine = pyttsx3.init('sapi5')
    Login_window.voices = Login_window.engine.getProperty('voices')
    Login_window.engine.setProperty('voice', Login_window.voices[1].id)

    Login_window.engine.say('Welcome Admin, Please Enter Your Login Details')
    Login_window.engine.runAndWait()

    def login(self):
        if (self.txtuser.get() == "" or self.txtpwd.get() == ""):
            self.engine.say('Please Enter Username and Password')
            self.engine.runAndWait()
        # messagebox.showerror("Error", "All Field Required!")
        else:
            conn = mysql.connector.connect(
                username='root', password='vishh@123', host='localhost', database='attendence_management')
            mycursor = conn.cursor()
            mycursor.execute("select * from login_tbl where Username=%s and Password=%s", (
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row = mycursor.fetchone()
            if row == None:
                self.engine.say('Invalid Username and Password')
                self.engine.runAndWait()
                # messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                self.engine.say('Do you want to enter')
                self.engine.runAndWait()
                open_min = messagebox.askyesno("YesNo", "You want to Enter?")
                if open_min > 0:
                    self.new_window = Toplevel(self)
                    self.app = Face_Recognition_system(self.new_window)
                    # Login_window.login_root.destroy()
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()

    background_img = Image.open("./img/login.png")
    background_img = background_img.resize(
        (1250, 680), Image.Resampling.LANCZOS)
    Login_window.photoimg1 = ImageTk.PhotoImage(background_img)

    background_img = Label(Login_window, image=Login_window.photoimg1)
    background_img.place(x=10, y=0, width=1250, height=680)

    # label1
    username = lb1 = Label(background_img, text="Username:", font=(
        "times new roman", 15, "bold"), fg="#4A5B5E", bg="white")
    username.place(x=835, y=330)

    # entry1
    Login_window.txtuser = ttk.Entry(
        background_img, font=("times new roman", 15, "bold"))
    Login_window.txtuser.place(x=940, y=330, width=180)

    # label2
    pwd = lb1 = Label(background_img, text="Password:", font=(
        "times new roman", 15, "bold"), fg="#023137", bg="white")
    pwd.place(x=835, y=390)

    # entry2
    Login_window.txtpwd = ttk.Entry(background_img, font=(
        "times new roman", 15, "bold"))
    Login_window.txtpwd.place(x=940, y=390, width=180)

    Login_btn = Button(background_img, command=login, text="LOGIN NOW", width=15, font=(
        "verdana", 10, "bold"), bg="#2DC6DB", fg="#023137")
    Login_btn.place(x=920, y=450, width=120, height=35)


splash_window.after(10000, Login_win)
        # self.root.overrideredirect(1)
splash_window.overrideredirect(1)

mainloop()
