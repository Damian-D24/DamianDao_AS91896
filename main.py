from tkinter import *
from tkinter import messagebox
import random

root = Tk()

# Adjust size of windows
root.geometry("1280x720")

# Adding an image file
bg = PhotoImage(file="images/homepage.png")

# Create canvas
canvas1=Canvas(root, width=1280, height=720)
canvas1.pack(fill="both", expand=True)

# Display the background
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Adding buttons
button1=Button(root, text="Let's Start")

# Display Buttons
button1_canvas=canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button1
)

button1.place(x=464.3, y=57)

button1.config(width=16, height=2)

root.mainloop()