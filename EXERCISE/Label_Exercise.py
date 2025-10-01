import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Styled Label Example")
root.geometry("400x200")

# Create a frame to center content
frame = ttk.Frame(root)
frame.pack(expand=True)

# Create label for "L" (underlined)
label_L = ttk.Label(frame, text="L", font=("Arial", 18, "underline"), foreground="#2c3e50")
label_L.pack(side="left")

# Create label for the rest of the text
label_rest = ttk.Label(frame, text="earning is fun!", font=("Arial", 18), foreground="#2c3e50")
label_rest.pack(side="left")

# Run the application
root.mainloop()
