# Midterm Part 2: PArt 2

from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

root = Tk()
root.title("CCSU Mobile App")
root.geometry("700x500")
root.resizable(0, 0)
root.configure(bg="light blue")

img = Image.open("ccsu-logo.png")
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")
data_img = img.getdata()
newData = []

for item in data_img:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)

logoLabel = Label(root, image=logo, bg="light blue")
logoLabel.place(x=20, y=10)

titleLabel = Label(root, text="CCSU Mobile App", font=("Arial", 18, "bold"), bg="light blue")
titleLabel.place(x=200, y=40)

data = pd.read_csv("examfile.csv")

lb = Label(root, justify="left", bg="light blue", font=("Arial", 11), anchor="w")
lb.place(x=130, y=220)

def calendar():
    df = pd.DataFrame(data, columns=["CalendarDate"])
    selected_rows = df[~df["CalendarDate"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def building():
    df = pd.DataFrame(data, columns=["Buildings"])
    selected_rows = df[~df["Buildings"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=["FacultyName"])
    selected_rows = df[~df["FacultyName"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))


def school_business():
    text = """School of Business Departments
 - Accounting
 - Finance
 - Management & Organization
 - Marketing
 - Management Information Systems (MIS)
 - Business Analytics"""
    lb.config(text=text)


def mis_department():
    text = """MIS Department Core Courses
 - Intro to MIS
 - Intro to MIS
 - Databases Management
 - Systems Analysis & Design
 - Business Analytics / Data Visualization
 - Network and Information Security
 - Project Management"""
    lb.config(text=text)

button1 = Button(root, text="Calendar", command=calendar, bg="light green", width=12)
button1.place(x=120, y=130)

button2 = Button(root, text="Buildings", command=building, bg="light green", width=12)
button2.place(x=260, y=130)

button3 = Button(root, text="Faculty", command=faculty, bg="light green", width=12)
button3.place(x=400, y=130)

button4 = Button(root, text='School of Business', command=school_business, bg="light green", width=16)
button4.place(x=180, y=180)

button5 = Button(root, text='MIS Department', command=mis_department, bg="light green", width=14)
button5.place(x=380, y=180)

root.mainloop()
