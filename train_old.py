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
        self.root.geometry("1430x790+0+0")
        self.root.title("Face Recognition System")

        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.engine.say('Click on Train Button, to train the Data sets')
        self.engine.runAndWait()

        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 28, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        b1 = Button(self.root, text="Train Data", command=self.train_classifier, font=(
            "times new roman", 15, "bold"), fg="blue", cursor="hand2")
        b1.place(x=550, y=100, width=180, height=40)

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
        messagebox.showinfo("Result", "Training dataset Complete!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
