import customtkinter as ctk
import pyglet
from tkinter import *
from tkinter import messagebox
import random

app = ctk.CTk()

# Loading Fonts
pyglet.font.add_file('fonts/BalsamiqSans-Regular.ttf')
pyglet.options['win32_gdi_font']
my_font=ctk.CTkFont(family="Balsamiq Sans", size=50)

# Adjust size of windows
app.geometry("1280x720")

# Adding an image file
bg = PhotoImage(file="images/homepage.png")

# Create canvas
canvas1=Canvas(app, width=1280, height=720)
canvas1.pack(fill="both", expand=True)

# Display the background
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Adding buttons
button1=ctk.CTkButton(app, text="Let's Start", bg_color="white", fg_color="#62c370", font=my_font, text_color="white", width=322, height=98, corner_radius=49)
button2=ctk.CTkButton(app, text="Exit")

# Display "Let's Start" Button
button1_canvas=canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button1
)

button1.place(x=479, y=580, anchor="sw")

# Display "Exit" Button
button2_canvas=canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button2
)

button2.place(x=1147, y=75, anchor="sw")

app.mainloop()