import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Test Entry Widget')
window.geometry('400x400')  

output_string = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string)

# Define the button command functions
def get_button1_text():
    output_string.set("You clicked Button 1")

def get_button2_text():
    output_string.set("You clicked Button 2")

# Buttons
button_1 = ttk.Button(master=window, text='BUTTON 1', command=get_button1_text)
button_2 = ttk.Button(master=window, text='BUTTON 2', command=get_button2_text)

# Pack widgets
button_1.pack()
button_2.pack()
output_label.pack()

window.mainloop()
