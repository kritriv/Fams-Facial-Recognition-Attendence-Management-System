from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
# --------------------------
from home import Face_Recognition_system
import os
import pyttsx3
import time


class Login:
    def __init__(self, login_root):
        def Speak(words):
            self.engine.say(words)
            self.engine.runAndWait()

        self.login_root = login_root
        self.login_root.title("Login")
        # window.iconbitmap("logo.ico")
        self.login_root.geometry("1280x700+0+0")

        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        # Assistance Speak Variable
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        Speak('Welcome Admin, Please Enter Your Login Details')

        background_img = Image.open("./img/login.png")
        background_img = background_img.resize(
            (1250, 680), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(background_img)

        background_img = Label(self.login_root, image=self.photoimg1)
        background_img.place(x=10, y=0, width=1250, height=680)

        # label1
        username = lb1 = Label(background_img, text="Username:", font=(
            "times new roman", 15, "bold"), fg="#4A5B5E", bg="white")
        username.place(x=835, y=330)

        # entry1
        self.txtuser = ttk.Entry(
            background_img, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=940, y=330, width=180)

        # label2
        pwd = lb1 = Label(background_img, text="Password:", font=(
            "times new roman", 15, "bold"), fg="#023137", bg="white")
        pwd.place(x=835, y=390)

        # entry2
        self.txtpwd = ttk.Entry(background_img, font=(
            "times new roman", 15, "bold"))
        self.txtpwd.place(x=940, y=390, width=180)

        Login_btn = Button(background_img, command=self.login, text="LOGIN NOW", width=15, font=(
            "verdana", 10, "bold"), bg="#2DC6DB", fg="#023137")
        Login_btn.place(x=920, y=450, width=120, height=35)

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
                    self.new_window = Toplevel(self.login_root)
                    self.app = Face_Recognition_system(self.new_window)
                    # self.login_root.destroy()
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()


if __name__ == "__main__":
    login_root = Tk()
    login_root.resizable(0, 0)
    app = Login(login_root)
    login_root.mainloop()


#    CREATE TABLE `attendence_management`.`login_tbl` (
#   `SR_No` INT NOT NULL,
#   `Username` VARCHAR(45) NULL,
#   `Password` VARCHAR(45) NULL,
#   PRIMARY KEY (`SR_No`));
