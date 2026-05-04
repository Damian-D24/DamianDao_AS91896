import customtkinter as ctk
import pyglet
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import random

app = ctk.CTk()

# Global Variables
names = []
asked = []
score = 0
qnum = 0

# Questions
# id: [question, option1, option2, option3, option4, correct_text, correct_option_number]
questions_answers = {
1: ["What kind of bird is this?",
    "Sparrow", "Pīwakawaka (Fantail)", "Miromiro", "Kea",
    "Pīwakawaka (Fantail)", 2],
2: ["What kind of bird is this?",
    "Kea", "Kākāpō", "Tūī", "Kererū",
    "Kererū", 4],
3: ["What kind of bird is this?",
    "Pukeko", "Miromiro", "Takahē", "Kea",
    "Pukeko", 1],
4: ["What kind of bird is this?",
    "Kererū", "Kea", "Kākāpō", "Kiwi",
    "Kea", 2],
5: ["What kind of bird is this?",
    "Takahē", "Whio (Blue Duck)", "Tūī", "Miromiro (Tomtit)",
    "Tūī", 3],
6: ["What kind of bird is this?",
    "Mohua (Yellowhead)", "Sparrow", "Tūī", "Miromiro (Tomtit)",
    "Mohua (Yellowhead)", 1],
7: ["What kind of bird is this?",
    "Black Robin", "Miromiro (Tomtit)", "Riroriro (Grey Warbler)", "Tuke (Rock Wren)",
    "Riroriro (Grey Warbler)", 3],
8: ["What kind of bird is this?",
    "Pukeko", "Takahē", "Kākā", "Weka",
    "Takahē", 2],
9: ["What kind of bird is this?",
    "Ruru", "Kōkako", "Penguin", "Kākāpō",
    "Takahē", 4],
10: ["What kind of bird is this?",
    "Kiwi", "Albatross", "Kakī (Black Stilt)", "Miromiro (Tomtit)",
    "Kiwi", 1],
}

# Loading Fonts
font_path = Path(__file__).parent / 'fonts/BalsamiqSans-Regular.ttf'
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file(str(font_path))
balsamiqsans = "Balsamiq Sans"
main_font=ctk.CTkFont(family=balsamiqsans, size=50, weight="bold")
exit_font=ctk.CTkFont(family=balsamiqsans, size=25)

# Adjust size of windows
app.geometry("1280x720")

#
# Defined Functions
#

# Close Window
def close_window():
    app.destroy()

# Start

#
# SCREEN 1
#
class QuizStart:
    # Adding an image file for the background
    bg = PhotoImage(file="images/homepage.png")
    # Create canvas
    canvas1=Canvas(app, width=1280, height=720)
    canvas1.pack(fill="both", expand=True)
    # Display the background
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    # Adding buttons
    button1=ctk.CTkButton(app, text="Let's Start", bg_color="white", fg_color="#62c370", font=main_font, text_color="white", width=322, height=100, corner_radius=50)
    button2=ctk.CTkButton(app, text="Exit", bg_color="#e46a4a", fg_color="white", font=exit_font, text_color="black", width=100, height=18, corner_radius=8, command=close_window)

    # Display "Let's Start" Button
    button1_canvas=canvas1.create_window(
        100,
        10,
        anchor="nw",
        window=button1
    )
    button1.place(x=479, y=582, anchor="sw")

    # Display "Exit" Button
    button2_canvas=canvas1.create_window(
        100,
        10,
        anchor="nw",
        window=button2
    )
    button2.place(x=1152, y=72, anchor="sw")

app.mainloop()