from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import DateEntry
import pyttsx3
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("890x600+350+50")
        self.root.title("FAMS - Student Management System")
        # root.overrideredirect(1)

        # Assistance Speak Variable
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.engine.say('You are now in Student Management System')
        self.engine.runAndWait()

        # ======== Function Declaration ====
        self.var_course = StringVar()
        self.var_stream = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_enroll = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_search = StringVar()

        # Background Image
        background_img = Image.open("./img/student_details.png")
        background_img = background_img.resize(
            (890, 600), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(background_img)

        background_img = Label(self.root, image=self.photoimg1)
        background_img.place(x=0, y=0, width=900, height=600)

        Top_frame = LabelFrame(background_img, bd=2, bg="white", relief=RIDGE, text="Student Entry", font=(
            "times new roman", 12, "bold"), fg="#2DC6DB")
        Top_frame.place(x=70, y=50, width=770, height=335)

        # current_course Frame
        current_course_frame = LabelFrame(Top_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=(
            "times new roman", 10, "bold"), fg="#2DC6DB")
        current_course_frame.place(x=90, y=10, width=600, height=100)

        # Course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 8, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 8, "bold"), state="readonly", width=20)
        course_combo["value"] = ("Select Course", "B.Tech", "M.Tech",
                                 "MCA", "B.Sc Honours", "BBA", "BBA-HA", "MBA", "MBA-HA")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=1, pady=10, sticky=W)

        # Stream
        stream_label = Label(current_course_frame, text="Stream", font=(
            "times new roman", 8, "bold"), bg="white")
        stream_label.grid(row=0, column=2, padx=10, sticky=W)

        stream_combo = ttk.Combobox(current_course_frame, textvariable=self.var_stream, font=(
            "times new roman", 8, "bold"), state="readonly", width=20)
        stream_combo["value"] = ("Select Stream", "Computer Science", "Info. Tech.",
                                 "Agriculture", "Chemical", "Mechanical", "ECE", "Business", "Others")
        stream_combo.current(0)
        stream_combo.grid(row=0, column=3, padx=1, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 8, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 8, "bold"), state="readonly", width=20)
        year_combo["value"] = ("Select Year", "Ist Year",
                               "IInd Year", "IIIrd Year", "IVth Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=1, pady=10, sticky=W)

        # Semester
        stream_label = Label(current_course_frame, text="Semester ", font=(
            "times new roman", 8, "bold"), bg="white")
        stream_label.grid(row=1, column=2, padx=10, sticky=W)

        stream_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 8, "bold"), state="readonly", width=20)
        stream_combo["value"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3",
                                 "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        stream_combo.current(0)
        stream_combo.grid(row=1, column=3, padx=1, pady=10, sticky=W)

        # Student Information Frame
        student_info_frame = LabelFrame(Top_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=(
            "times new roman", 10, "bold"), fg="#2DC6DB")
        student_info_frame.place(x=20, y=120, width=720, height=180)

        # student ID
        student_ID_label = Label(student_info_frame, text="Student ID", font=(
            "times new roman", 8, "bold"), bg="white")
        student_ID_label.grid(row=0, column=0, padx=5, sticky=W)

        student_ID_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_id, width=15, font=("times new roman", 10, "bold"))
        student_ID_entry.grid(row=0, column=1, padx=5, sticky=W)

        # student Name
        student_name_label = Label(student_info_frame, text="Student Name", font=(
            "times new roman", 8, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=5, sticky=W)

        student_name_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_name, width=15, font=("times new roman", 10, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, sticky=W)

        # Enrollment no.
        student_enroll_label = Label(student_info_frame, text="Enrollment No", font=(
            "times new roman", 8, "bold"), bg="white")
        student_enroll_label.grid(row=0, column=4, padx=5, sticky=W)

        student_enroll_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_enroll, width=15, font=("times new roman", 10, "bold"))
        student_enroll_entry.grid(row=0, column=5, padx=5, pady=5, sticky=W)

        # Roll no.
        student_rollno_label = Label(student_info_frame, text="Roll No", font=(
            "times new roman", 8, "bold"), bg="white")
        student_rollno_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        student_rollno_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_roll, width=15, font=("times new roman", 10, "bold"))
        student_rollno_entry.grid(row=1, column=1, padx=5, sticky=W)

        # Date of Birth
        student_dob_label = Label(student_info_frame, text="Date of Birth", font=(
            "times new roman", 8, "bold"), bg="white")
        student_dob_label.grid(row=1, column=2, padx=5, sticky=W)

        student_dob_entry = DateEntry(student_info_frame, selectmode='year',
                                      textvariable=self.var_dob, width=15, font=("times new roman", 10, "bold"))
        # student_dob_entry = ttk.Entry(
        #     student_info_frame, textvariable=self.var_dob, width=15, font=("times new roman", 12, "bold"))
        student_dob_entry.grid(row=1, column=3, padx=5, sticky=W)

        # Gender
        student_gender_label = Label(student_info_frame, text="Gender", font=(
            "times new roman", 8, "bold"), bg="white")
        student_gender_label.grid(row=1, column=4, padx=5, sticky=W)

        gender_combo = ttk.Combobox(student_info_frame, textvariable=self.var_gender, font=(
            "times new roman", 10, "bold"), state="readonly", width=15)
        gender_combo["value"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=5, padx=5, sticky=W)

        # Mobile no.
        student_mobileno_label = Label(student_info_frame, text="Mobile No", font=(
            "times new roman", 8, "bold"), bg="white")
        student_mobileno_label.grid(row=3, column=0, padx=5, sticky=W)

        student_mobileno_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_mobile, width=15, font=("times new roman", 10, "bold"))
        student_mobileno_entry.grid(row=3, column=1, padx=5, sticky=W)

        # Email ID
        student_email_label = Label(student_info_frame, text="Email ID", font=(
            "times new roman", 8, "bold"), bg="white")
        student_email_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        student_email_entry = ttk.Entry(
            student_info_frame, textvariable=self.var_email, width=15, font=("times new roman", 10, "bold"))
        student_email_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Radio btns
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            student_info_frame, variable=self.var_radio1, text="Take Photo", value="Yes")
        radiobtn1.grid(row=3, column=4, padx=10, pady=10)

        radiobtn2 = ttk.Radiobutton(
            student_info_frame, variable=self.var_radio1, text="No Photo", value="No")
        radiobtn2.grid(row=3, column=5, pady=10)

        # Buttons Frame 1
        btn_frame1 = Frame(Top_frame, relief=RIDGE, bg="white")
        btn_frame1.place(x=70, y=260, width=580, height=35)

        save_btn = Button(btn_frame1, command=self.add_data, text="Save", width=10, font=(
            "times new roman", 10, "bold"), bg="#2DC6DB", fg="#023137")
        save_btn.grid(row=0, column=0, padx=10)

        Update_btn = Button(btn_frame1, command=self.update_data, text="Update", width=10, font=(
            "times new roman", 10, "bold"), bg="#E4FF3E", fg="#023137")
        Update_btn.grid(row=0, column=1, padx=10)

        Delete_btn = Button(btn_frame1, command=self.Delete_data, text="Delete", width=10, font=(
            "times new roman", 10, "bold"), bg="#FF705C", fg="#023137")
        Delete_btn.grid(row=0, column=2, padx=10)

        Reset_btn = Button(btn_frame1, command=self.reset_data, text="Reset", width=10, font=(
            "times new roman", 10, "bold"), bg="#30FFC1", fg="#023137")
        Reset_btn.grid(row=0, column=4, padx=10)

        # Buttons Frame 2
        btn_frame2 = Frame(Top_frame, relief=RIDGE, bg="white")
        btn_frame2.place(x=480, y=260, width=200, height=35)

        take_photo_btn = Button(btn_frame2, command=self.gernerate_dataset,  text="Take Photos", width=10, font=(
            "times new roman", 10, "bold"), bg="#FF5C97", fg="#023137")
        take_photo_btn.grid(row=0, column=1)

        Data_view_btn = Button(btn_frame2, command=self.datasets_img, text="Data-Img", width=10, font=(
            "times new roman", 10, "bold"), bg="white", fg="#023137")
        Data_view_btn.grid(row=0, column=2, padx=20)

        Bottom_frame = LabelFrame(background_img, bd=2, bg="white", relief=RIDGE, text="Student Details Table", font=(
            "times new roman", 12, "bold"), fg="#2DC6DB")
        Bottom_frame.place(x=70, y=400, width=770, height=150)

        # TableFrame
        table_frame = Frame(Bottom_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=20, y=10, width=720, height=100)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("Student_ID", "Name", "Course", "Stream", "Year", "Semester", "Enroll",
                                          "Roll", "Dob", "Gender", "Mobile", "Email", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Student_ID", text="Student ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Stream", text="Stream")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Enroll", text="Enroll No")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Dob", text="Date of birth")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Mobile", text="Mobile No")
        self.student_table.heading("Email", text="Email Id")
        self.student_table.heading("Photo", text="Photo Status")

        self.student_table.column("Student_ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Stream", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Enroll", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Dob", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Mobile", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ======== Function Declaration ====

    # Push or Add Data to Database

    def add_data(self):
        if self.var_course.get() == "Select Course" or self.var_stream.get() == "Select Stream" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_enroll.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_radio1.get() == "":
            self.engine.say('Please Fill All the Required Fields')
            self.engine.runAndWait()
            # messagebox.showerror(
            #     "Error!", "All Fields are Reqired", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="vishh@123", database="attendence_management")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_stream.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_enroll.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_radio1.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()

                self.engine.say('Student Details Added Successfully')
                self.engine.runAndWait()
                # messagebox.showinfo(
                #     "Success", "Student Details Added Successfully", parent=self.root)
            except Exception as es:
                self.engine.say('Something is wrong')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # fetch Data from Database

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="vishh@123", database="attendence_management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor data to fields

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_course.set(data[2]),
        self.var_stream.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_enroll.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_mobile.set(data[10]),
        self.var_email.set(data[11]),
        self.var_radio1.set(data[12])

    # Update Function

    def update_data(self):
        if self.var_course.get() == "Select Course" or self.var_stream.get() == "Select Stream" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_enroll.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_radio1.get() == "":
            self.engine.say('All Fields are Reqired')
            self.engine.runAndWait()
            # messagebox.showerror(
            #     "Error!", "All Fields are Reqired", parent=self.root)
        else:
            try:
                self.engine.say('Do you want to update this Student details')
                self.engine.runAndWait()
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this Student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="vishh@123", database="attendence_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student set Name=%s,Course=%s,Stream=%s,Year=%s,Semester=%s,Enroll=%s,Roll=%s,Dob=%s,Gender=%s,Mobile=%s,Email=%s,Photo=%s WHERE Student_ID=%s", (
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_stream.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_enroll.get(),
                        self.var_roll.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                self.engine.say('Student Detail Successfully Updated')
                self.engine.runAndWait()
                # messagebox.showinfo(
                #     "Success", "Student Detail Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                self.engine.say('Something is wrong')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # Delete Function

    def Delete_data(self):
        if self.var_id.get() == "":
            self.engine.say('Student Id must be Required')
            self.engine.runAndWait()
            # messagebox.showerror(
            #     "Error!", "Student Id must be Required", parent=self.root)
        else:
            try:
                self.engine.say(
                    'Do you really want to Delete this Student Details')
                self.engine.runAndWait()
                delete = messagebox.askyesno(
                    "Delete?", "Do you want to Delete this Student Details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="vishh@123", database="attendence_management")
                    my_cursor = conn.cursor()
                    sql = "DELETE from student WHERE Student_ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.engine.say('Successfully Deleted Student Details')
                self.engine.runAndWait()
                # messagebox.showinfo(
                #     "Deleted", "Successfully Deleted Student Details", parent=self.root)

            except Exception as es:
                self.engine.say('Something is wrong')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # Reset Function

    def reset_data(self):
        self.var_course.set("Select Course"),
        self.var_stream.set("Select Stream"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_enroll.set(""),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_gender.set("Select Gender"),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")

# ===========================Search Data===================
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            self.engine.say('Select Combo option and enter entry')
            self.engine.runAndWait()
            messagebox.showerror(
                "Error", "Select Combo option and enter entry", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    username='root', password='vishh@123', host='localhost', database='face_recognition')
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Course,Stream, Year,Semester,Enoll, Roll, Dob, Gender,Mobile,Email,Photo FROM student where Roll='" + \
                    str(self.var_search.get()) + "'"
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        self.engine.say('Data Not Found')
                        self.engine.runAndWait()
                        messagebox.showerror(
                            "Error", "Data Not Found", parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                self.engine.say('Something is wrong')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ========== Take Photo Sample =============

    def gernerate_dataset(self):
        if self.var_course.get() == "Select Course" or self.var_stream.get() == "Select Stream" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_enroll.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_radio1.get() == "":
            self.engine.say('All Fields are Reqired')
            self.engine.runAndWait()
            messagebox.showerror(
                "Error!", "All Fields are Reqired", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="vishh@123", database="attendence_management")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE student set Name=%s,Course=%s,Stream=%s,Year=%s,Semester=%s,Enroll=%s,Roll=%s,Dob=%s,Gender=%s,Mobile=%s,Email=%s,Photo=%s WHERE Student_ID=%s", (

                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_stream.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_enroll.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============= Load predefined data on face frontals from open cv2====
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # scaling factor - 1.3   & minimum nwighbor -5
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (250, 250))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data-img/Student." + \
                            str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.engine.say('Generating  dat sets Completed')
                self.engine.runAndWait()
                # messagebox.showinfo(
                #     "Result", "Generating  dat sets Completed!")

            except Exception as es:
                self.engine.say('Something is wrong')
                self.engine.runAndWait()
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

# ============= Funtions =========
    def datasets_img(self):
        os.startfile("data-img")


if __name__ == "__main__":
    root = Tk()
    # root.resizable(0, 0)
    # root.overrideredirect(1)
    obj = Student(root)
    root.mainloop()


# CREATE TABLE `attendence_management`.`student` (
#   `Student_ID` INT NOT NULL,
#   `Name` VARCHAR(45) NULL,
#   `Course` VARCHAR(45) NULL,
#   `Stream` VARCHAR(45) NULL,
#   `Year` VARCHAR(45) NULL,
#   `Semester` VARCHAR(45) NULL,
#   `Enroll` VARCHAR(45) NULL,
#   `Roll` VARCHAR(45) NULL,
#   `Dob` VARCHAR(45) NULL,
#   `Gender` VARCHAR(45) NULL,
#   `Mobile` VARCHAR(45) NULL,
#   `Email` VARCHAR(45) NULL,
#   `Photo` VARCHAR(45) NULL,
#   PRIMARY KEY (`Student_ID`));
