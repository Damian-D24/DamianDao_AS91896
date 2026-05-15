import PIL
import customtkinter as ctk
import pyglet
from pathlib import Path
from tkinter import *
from PIL import Image
from tkinter import messagebox
import random

root = ctk.CTk()

# Global Variables
names = []
asked = []
score = 0
qnum = 0

# Questions
# id: [question, option1, option2, option3, option4, correct_text, correct_option_number, image]
questions_answers = {
1: ["What kind of bird is this?",
    "Sparrow", "Pīwakawaka", "Miromiro", "Kea",
    "Pīwakawaka", 2, "images/birds/piwakawaka.jpg"],
2: ["What kind of bird is this?",
    "Kea", "Kākāpō", "Tūī", "Kererū",
    "Kererū", 4, "images/birds/kereru.png"],
3: ["What kind of bird is this?",
    "Pukeko", "Miromiro", "Takahē", "Kea",
    "Pukeko", 1, "images/birds/pukeko.jpg"],
4: ["What kind of bird is this?",
    "Kererū", "Kea", "Kākāpō", "Kiwi",
    "Kea", 2, "images/birds/kea.jpg"],
5: ["What kind of bird is this?",
    "Takahē", "Whio", "Tūī", "Miromiro",
    "Tūī", 3, "images/birds/tui.png"],
6: ["What kind of bird is this?",
    "Mohua", "Sparrow", "Tūī", "Miromiro",
    "Mohua", 1, "images/birds/mohua.jpg"],
7: ["What kind of bird is this?",
    "Black Robin", "Miromiro", "Riroriro", "Tuke",
    "Riroriro", 3, "images/birds/riroriro.jpg"],
8: ["What kind of bird is this?",
    "Pukeko", "Takahē", "Kākā", "Weka",
    "Takahē", 2, "images/birds/takahe.jpg"],
9: ["What kind of bird is this?",
    "Ruru", "Kōkako", "Penguin", "Kākāpō",
    "Kākāpō", 4, "images/birds/kakapo.jpg"],
10: ["What kind of bird is this?",
    "Kiwi", "Albatross", "Kakī", "Miromiro",
    "Kiwi", 1, "images/birds/kiwi.jpg"],
}

# Loading Fonts
font_path = Path(__file__).parent / 'fonts/BalsamiqSans-Regular.ttf'
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file(str(font_path))
balsamiqsans = "Balsamiq Sans"

main_font=ctk.CTkFont(family=balsamiqsans, size=50, weight="bold")
entry_font_title=ctk.CTkFont(family=balsamiqsans, size=18)
entry_font=ctk.CTkFont(family=balsamiqsans, size=14)
exit_font=ctk.CTkFont(family=balsamiqsans, size=25)

answer_font=ctk.CTkFont(family=balsamiqsans, size=28, weight="bold")
main_exit_font=ctk.CTkFont(family=balsamiqsans, size=27)
questionnumber_font=ctk.CTkFont(family=balsamiqsans, size=40, weight="bold")

# Adjust size of windows
root.geometry("1280x720")

#
# DEFINED FUNCTIONS
#

# Close Window
def close_window():
    root.destroy()

def randomiser():
    # Selects a random question that hasn't been asked yet
    global qnum
    qnum = random.randint(1, len(questions_answers))
    if qnum not in asked:
        asked.append(qnum)
    else:
        randomiser()

#
# SCREEN 1
#
class QuizStart:
    def __init__(self, parent):
        self.parent = parent
        # Create Frame
        self.frame=Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)
        # Display the background
        bg = PIL.Image.open("images/homepage.png")
        bg_image=ctk.CTkImage(light_image=bg,dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Name Input Entry
        self.entrylabel = ctk.CTkLabel(self.frame, font=entry_font_title, text="Please enter your name!", fg_color="white")
        self.entrylabel.place(x=550, y=403)
        self.entryname = Entry(self.frame, font=entry_font, relief="solid")
        self.entryname.place(x=570, y=443)
        # Adding Start and Exit Button
        self.button1=ctk.CTkButton(self.frame, text="Let's Start",
                                   bg_color="white", fg_color="#62c370", font=main_font, text_color="white",
                                   width=322, height=100, corner_radius=50, command=self.start_quiz)
        self.button2=ctk.CTkButton(self.frame, text="Exit",
                                   bg_color="#e46a4a", fg_color="white", font=exit_font, text_color="black",
                                   width=100, height=18, corner_radius=8, command=close_window)
        # Display "Let's Start" Button
        self.button1.place(x=479, y=582, anchor="sw")

        # Display "Exit" Button
        self.button2.place(x=1152, y=72, anchor="sw")
    # Function to Start the Quiz
    def start_quiz(self):
        name = self.entryname.get().strip()
        if name:
            names.append(name)
            self.frame.destroy()
            Quiz(self.parent)
        else:
            messagebox.showerror("Error", "Please enter your name.")

#
# SCREEN 2
#
class Quiz:
    def __init__(self, parent):
        self.parent = parent
        # Create Frame
        self.frame=Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)
        # Display the background
        # Adding background images
        bg = PIL.Image.open("images/question.png")
        bg_image=ctk.CTkImage(light_image=bg,dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Adding Question Count
        self.questioncounter = ctk.CTkLabel(self.frame, text=f"{len(asked) + 1}/10", font=questionnumber_font, fg_color="#62c370",
                                            text_color="white")
        self.questioncounter.place(x=119, y=110)
        # Adding Exit Button
        self.button2=ctk.CTkButton(self.frame, text="Exit",
                                   bg_color="#e46a4a", fg_color="white", font=main_exit_font, text_color="black",
                                   width=94, height=14, corner_radius=7, command=close_window)
        # Display "Exit" Button
        self.button2.place(x=1080, y=153, anchor="sw")

        #Setting up Randomiser to Randomise Questions
        randomiser()
        self.var = IntVar(value=0)
        # Adding Answer Option Buttons
        Radiobutton(self.frame,
                    text=questions_answers[qnum][1],
                    variable=self.var, value=1, width=11, height=1,
                    font=answer_font, relief="sunken",
                    justify="left", bg="#62c370", fg="white", activebackground="#f2c409", selectcolor="black",
                    anchor="w").place(x=109, y=257)

        Radiobutton(self.frame,
                    text=questions_answers[qnum][2],
                    variable=self.var, value=2, width=11, height=1,
                    font=answer_font, relief="sunken",
                    justify="left", bg="#62c370", fg="white", activebackground="#f2c409", selectcolor="black",
                    anchor="w").place(x=956, y=257)

        Radiobutton(self.frame,
                    text=questions_answers[qnum][3],
                    variable=self.var, value=3, width=11, height=1,
                    font=answer_font, relief="sunken",
                    justify="left", bg="#62c370", fg="white", activebackground="#f2c409", selectcolor="black",
                    anchor="w").place(x=109, y=470)

        Radiobutton(self.frame,
                    text=questions_answers[qnum][4],
                    variable=self.var, value=4, width=11, height=1,
                    font=answer_font, relief="sunken",
                    justify="left", bg="#62c370", fg="white", activebackground="#f2c409", selectcolor="black",
                    anchor="w").place(x=956, y=470)
        # Adding image of bird
        bird = PIL.Image.open(questions_answers[qnum][8])
        bg_image = ctk.CTkImage(light_image=bg, dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


quiz_instance = QuizStart(root)
root.mainloop()