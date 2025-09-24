#Ike Testing
import tkinter as tk
from tkinter import ttk

# This section creates the tkinter Window and adds the required elements to it
window = tk.Tk()
window.title('Tkinter Lavel Widget')
window.geometry('400x400')

#This is our label
output_label = ttk.Label(master = window, text = 'This is my label', font = 'Calibri 24 bold')

#Pack elements in frames ready to push onto form/window
output_label.pack();

# Run the program to generate window with all packed elements for user interaction
window.mainloop()
