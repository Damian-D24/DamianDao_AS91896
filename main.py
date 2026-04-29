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
button2=Button(root, text="Exit", borderwidth=0, highlightthickness=0)

# Display "Let's Start" Button
button1_canvas=canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button1
)

button1.place(x=510, y=560, anchor="sw")

button1.config(width=32, height=4)

# Display "Exit" Button
button2_canvas=canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button2
)

button2.place(x=1147, y=75, anchor="sw")
button2.config(width=15, height=3)

root.mainloop()