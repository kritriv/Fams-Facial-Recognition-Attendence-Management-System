# Importing the tkinter library
from tkinter import *

# Create an instance of tkinter frame
splash_win = Tk()

# Set the title of the window
splash_win.title("Splash Screen Example")

# Define the size of the window or frame
splash_win.geometry("700x200")

# Remove border of the splash Window

splash_win.overrideredirect(True)

# Define the label of the window
splash_label = Label(splash_win, text="Hello World!", fg="green",
                     font=('Times New Roman', 40)).pack(pady=20)


def mainWin():
    splash_win.destroy()
    win = Tk()
    win.title("Main Window")
    win.geometry("700x200")
    win_label = Label(win, text="Main Window", font=(
        'Helvetica', 25), fg="red").pack(pady=20)

# Splash Window Timer


splash_win.after(5000, mainWin)

mainloop()
