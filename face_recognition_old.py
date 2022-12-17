from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import time
import pyttsx3


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("Face Recognition System")

        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.engine.say(
            'Click on Recognition Button, to recognize the students')
        self.engine.runAndWait()

        title_lbl = Label(self.root, text="Face Recognition",
                          font=("times new roman", 28, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=60)

        b1 = Button(self.root, text="Face Recognition", command=self.face_recog, font=(
            "times new roman", 15, "bold"), fg="blue", cursor="hand2")
        b1.place(x=550, y=100, width=180, height=40)

    # =====================Attendance===================

    def mark_attendance(self, i, r, n, d, al):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            if n in name_list:
                print("already Present")
            else:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i} {r} {n} {al} {d} {dtString} {d1} Present")

 # ================face recognition==================

    def face_recog(self):
        self.engine.say('Recognition mode is on')
        self.engine.runAndWait()

        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="vishh@123", database="attendence_management")
                cursor = conn.cursor()

                cursor.execute(
                    "select * from student where Student_ID="+str(id))
                al = cursor.fetchall()

                cursor.execute(
                    "select Name from student where Student_ID="+str(id))
                n = cursor.fetchone()
                # n="+".join(n)

                cursor.execute(
                    "select Roll from student where Student_ID="+str(id))
                r = cursor.fetchone()
                # r="+".join(r)

                cursor.execute(
                    "select Course from student where Student_ID="+str(id))
                d = cursor.fetchone()
                # d="+".join(d)

                cursor.execute(
                    "select Student_ID from student where Student_ID="+str(id))
                i = cursor.fetchone()
                # i="+".join(i)

                if confidence > 78:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 1)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 1)
                    cv2.putText(
                        img, f"Roll No:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 1)
                    cv2.putText(
                        img, f"Course:{d}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 1)
                    self.mark_attendance(i, r, n, d, al)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-8),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 1)

                coord = [x, y, w, y]

            return coord

        # ========== Recognize Function
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
        self.engine.say('Recognition mode is off')
        self.engine.runAndWait()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
