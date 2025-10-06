import tkinter as tk
from tkinter import *
from tkinter import ttk

# Function to calculate and display grade
def calculate_grade():
    try:
        mark = float(MarkEntry.get())
        if mark >= 90:
            grade = "A+"
        elif mark >= 80:
            grade = "A"
        elif mark >= 70:
            grade = "B"
        elif mark >= 60:
            grade = "C"
        elif mark >= 50:
            grade = "D"
        else:
            grade = "F"
        GradeOutput.config(text=grade)
        return grade
    except ValueError:
        GradeOutput.config(text="Invalid")
        return None

# Function to submit and insert into table
def submit_data():
    grade = calculate_grade()
    if grade:
        fname = FirstNameEntry.get()
        lname = LastNameEntry.get()
        subject = SubjectEntry.get()
        mark = MarkEntry.get()
        # Insert data into table
        tree.insert("", "end", values=(fname, lname, subject, mark, grade))
        # Clear fields
        FirstNameEntry.delete(0, END)
        LastNameEntry.delete(0, END)
        SubjectEntry.delete(0, END)
        MarkEntry.delete(0, END)
        GradeOutput.config(text="")

# Create main window
window = Tk()
window.geometry("1000x750")
window.title("SIMPLE GRADING SYSTEM")

# Title Label
title = tk.Label(
    master=window,
    text='Enter Student Grade:',
    font='Nunito 25 bold',
    borderwidth=1,
    relief="solid"
)
title.place(x=200, y=50, width=600, height=75)

# First Name
FirstNameLabel = tk.Label(window, text='First Name:', font='Nunito 13', borderwidth=1, relief="solid")
FirstNameLabel.place(x=200, y=150, width=200, height=40)
FirstNameEntry = tk.Entry(window, borderwidth=1, relief="solid")
FirstNameEntry.place(x=450, y=150, width=275, height=38)

# Last Name
LastNameLabel = tk.Label(window, text='Last Name:', font='Nunito 13', borderwidth=1, relief="solid")
LastNameLabel.place(x=200, y=210, width=200, height=40)
LastNameEntry = tk.Entry(window, borderwidth=1, relief="solid")
LastNameEntry.place(x=450, y=210, width=275, height=38)

# Subject
SubjectLabel = tk.Label(window, text='Subject:', font='Nunito 13', borderwidth=1, relief="solid")
SubjectLabel.place(x=200, y=270, width=200, height=40)
SubjectEntry = tk.Entry(window, borderwidth=1, relief="solid")
SubjectEntry.place(x=450, y=270, width=275, height=38)

# Mark
MarkLabel = tk.Label(window, text='Mark (%):', font='Nunito 13', borderwidth=1, relief="solid")
MarkLabel.place(x=200, y=330, width=200, height=40)
MarkEntry = tk.Entry(window, borderwidth=1, relief="solid")
MarkEntry.place(x=450, y=330, width=275, height=38)

# Grade
GradeLabel = tk.Label(window, text='GRADE', font='Nunito 13 bold', borderwidth=1, relief="solid", fg='green')
GradeLabel.place(x=300, y=430, width=150, height=40)
GradeOutput = tk.Label(window, text='', font='Nunito 16 bold', fg='green')
GradeOutput.place(x=480, y=430, width=100, height=40)

# Submit Button
SubmitButton = tk.Button(
    master=window,
    text="SUBMIT",
    font='Nunito 13 bold',
    bg="white",
    fg="black",
    relief="solid",
    borderwidth=1,
    command=submit_data
)
SubmitButton.place(x=650, y=430, width=100, height=40)

# Table Frame
table_frame = tk.Frame(window, borderwidth=1, relief="solid")
table_frame.place(x=150, y=500, width=700, height=200)

# Scrollbar
scrollbar = tk.Scrollbar(table_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Treeview (Table)
tree = ttk.Treeview(
    table_frame,
    columns=("First Name", "Last Name", "Subject", "Mark (%)", "Grade"),
    show="headings",
    yscrollcommand=scrollbar.set,
    height=8
)

tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Subject", text="Subject")
tree.heading("Mark (%)", text="Mark (%)")
tree.heading("Grade", text="Grade")

tree.column("First Name", width=120, anchor=CENTER)
tree.column("Last Name", width=120, anchor=CENTER)
tree.column("Subject", width=120, anchor=CENTER)
tree.column("Mark (%)", width=120, anchor=CENTER)
tree.column("Grade", width=80, anchor=CENTER)

tree.pack(fill=BOTH, expand=True)
scrollbar.config(command=tree.yview)

# Run program
window.mainloop()
