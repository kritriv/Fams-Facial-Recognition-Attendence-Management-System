from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import pyttsx3


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("890x600+350+50")
        self.root.title("FAMS - Trainig Data sets")
        # root.overrideredirect(1)

        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.engine.say('click on Train Button, to train the Data sets')
        self.engine.runAndWait()

        # Background Image
        background_img = Image.open("./img/student_details.png")
        background_img = background_img.resize(
            (890, 600), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(background_img)

        background_img = Label(self.root, image=self.photoimg1)
        background_img.place(x=0, y=0, width=900, height=600)

        train_btn = Button(background_img, command=self.train_classifier, text="Train Datasets", width=15, font=(
            "verdana", 10, "bold"), cursor="hand2", bg="#2DC6DB", fg="#023137")
        train_btn.place(x=390, y=450, width=120, height=35)

    def train_classifier(self):
        self.engine.say('Training in process please wait')
        self.engine.runAndWait()
        data_dir = ("data-img")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ===== Train the classifier

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        self.engine.say('Training dataset Complete')
        self.engine.runAndWait()
        # messagebox.showinfo("Result", "Training dataset Complete!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
