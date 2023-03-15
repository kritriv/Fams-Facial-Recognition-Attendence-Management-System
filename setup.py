import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Fams - Facial Recognition Attendance Management System",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'img','data-img','database','attendance_record']}},
    version = "1.0",
    description = "Fams - Facial Recognition Attendance Management System | Developed By Vishal Saraiwal",
    executables = executables
    )