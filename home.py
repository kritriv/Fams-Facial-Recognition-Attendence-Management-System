from pyclbr import Function
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
import pyttsx3


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title(
            "FAMS - Facial Recognition Attendance Management System")
        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.engine.say(
            'Welcome to Fams Facial Recognition Attendance Management System')
        self.engine.runAndWait()

        # Background Image
        background_img = Image.open("./img/Home.png")
        background_img = background_img.resize(
            (1250, 680), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(background_img)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=10, y=0, width=1250, height=680)

        # Btn Image 1 - Home
        Home_btn = Image.open("./img/Home_btn.png")
        Home_btn = Home_btn.resize((260, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(Home_btn)

        Home_btn = Button(bg_img, image=self.photoimg2, borderwidth=0,
                          highlightthickness=0, relief="flat", cursor="hand2", bd=0)
        Home_btn.place(x=38, y=200, width=260, height=36)

        # Btn Image 2 - Student Management System
        Student_btn = Image.open("./img/Student_btn.png")
        Student_btn = Student_btn.resize((260, 40), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(Student_btn)

        Student_btn = Button(bg_img, image=self.photoimg3,
                             command=self.student_details, cursor="hand2", relief=RIDGE, bd=0)
        Student_btn.place(x=38, y=255, width=260, height=40)

        # Btn Image 3 - Attendance Management System
        Attendance_btn = Image.open("./img/Attendance_btn.png")
        Attendance_btn = Attendance_btn.resize(
            (260, 40), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(Attendance_btn)

        Attendance_btn = Button(bg_img, image=self.photoimg4,
                                command=self.attendance_mng, cursor="hand2", relief=RIDGE, bd=0)
        Attendance_btn.place(x=38, y=310, width=260, height=36)

        # Btn Image 4 - Recognition
        Recognition_btn = Image.open("./img/Recognition_btn.png")
        Recognition_btn = Recognition_btn.resize(
            (260, 40), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(Recognition_btn)

        Recognition_btn = Button(bg_img, image=self.photoimg5,
                                 command=self.recognition_img, cursor="hand2", relief=RIDGE, bd=0)
        Recognition_btn.place(x=38, y=365, width=260, height=36)

        # Btn Image 7 - Developer
        Developer_btn = Image.open("./img/Developer_btn.png")
        Developer_btn = Developer_btn.resize(
            (150, 40), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(Developer_btn)

        Developer_btn = Button(bg_img, image=self.photoimg8, command=self.Developer_fun,
                               cursor="hand2", relief=RIDGE, bd=0)
        Developer_btn.place(x=90, y=545, width=150, height=36)

        # Btn Image 8 - Log Out
        logout_btn = Image.open("./img/logout_btn.png")
        logout_btn = logout_btn.resize((150, 40), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(logout_btn)

        logout_btn = Button(bg_img, image=self.photoimg9, command=self.Close,
                            cursor="hand2", relief=RIDGE, bd=0)
        logout_btn.place(x=90, y=600, width=150, height=36)

    # Button Functions

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def attendance_mng(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def recognition_img(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Developer_fun(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def datasets_img(self):
        os.startfile("data-img")

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    # root.resizable(0,0)
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
