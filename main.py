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
    "Pīwakawaka", 2, "images/birds/piwakawaka.png"],
2: ["What kind of bird is this?",
    "Kea", "Kākāpō", "Tūī", "Kererū",
    "Kererū", 4, "images/birds/kereru.png"],
3: ["What kind of bird is this?",
    "Pukeko", "Miromiro", "Takahē", "Kea",
    "Pukeko", 1, "images/birds/pukeko.png"],
4: ["What kind of bird is this?",
    "Kererū", "Kea", "Kākāpō", "Kiwi",
    "Kea", 2, "images/birds/kea.png"],
5: ["What kind of bird is this?",
    "Takahē", "Whio", "Tūī", "Miromiro",
    "Tūī", 3, "images/birds/tui.png"],
6: ["What kind of bird is this?",
    "Mohua", "Sparrow", "Tūī", "Miromiro",
    "Mohua", 1, "images/birds/mohua.png"],
7: ["What kind of bird is this?",
    "Black Robin", "Miromiro", "Riroriro", "Tuke",
    "Riroriro", 3, "images/birds/riroriro.png"],
8: ["What kind of bird is this?",
    "Pukeko", "Takahē", "Kākā", "Weka",
    "Takahē", 2, "images/birds/takahe.png"],
9: ["What kind of bird is this?",
    "Ruru", "Kōkako", "Penguin", "Kākāpō",
    "Kākāpō", 4, "images/birds/kakapo.png"],
10: ["What kind of bird is this?",
    "Kiwi", "Albatross", "Kakī", "Miromiro",
    "Kiwi", 1, "images/birds/kiwi.png"],
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
        # Pick a question before using qnum
        randomiser()
        # Create Frame
        self.frame=Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)
        # Display the background
        # Adding background images
        bg = PIL.Image.open(questions_answers[qnum][7])
        bg_image=ctk.CTkImage(light_image=bg,dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Adding Question Count
        self.questioncounter = ctk.CTkLabel(self.frame, text=f"{len(asked)}/10", font=questionnumber_font, fg_color="#62c370",
                                            text_color="white")
        self.questioncounter.place(x=119, y=110)
        # Adding Exit Button
        self.button2=ctk.CTkButton(self.frame, text="Exit",
                                   bg_color="#e46a4a", fg_color="white", font=main_exit_font, text_color="black",
                                   width=94, height=14, corner_radius=7, command=close_window)
        # Display "Exit" Button
        self.button2.place(x=1080, y=153, anchor="sw")

        self.var = IntVar(value=0)

        # Adding Answer Option Buttons
        self.option1 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][1],
                    variable=self.var, value=1, width=11, height=1,
                    font=answer_font,
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option1.place(x=109, y=257)

        self.option2 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][2],
                    variable=self.var, value=2, width=11, height=1,
                    font=answer_font,
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option2.place(x=956, y=257)

        self.option3 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][3],
                    variable=self.var, value=3, width=11, height=1,
                    font=answer_font,
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option3.place(x=109, y=470)

        self.option4 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][4],
                    variable=self.var, value=4, width=11, height=1,
                    font=answer_font,
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option4.place(x=956, y=470)

        # Submit Button
        self.submit_button = ctk.CTkButton(self.frame, text="Submit",
                                           bg_color="white", fg_color="#62c370", font=main_font, text_color="white",
                                           width=250, height=80, corner_radius=40,
                                           command=self.submit_answer)
        self.submit_button.place(x=640, y=640, anchor="center")


    def submit_answer(self):
        selected = self.var.get()
        if selected == 0:
            messagebox.showerror("Error", "Please select an answer.")
            return
        global score
        if selected == questions_answers[qnum][6]:
            score += 1
        if len(asked) >= 10:
            messagebox.showinfo("Quiz Complete", f"{names[-1]}, you scored {score}/10!")
            close_window()
        else:
            self.frame.destroy()
            Quiz(self.parent)

    def highlight_selected(self):
        options = [self.option1, self.option2, self.option3, self.option4]
        selected = self.var.get()
        for i, opt in enumerate(options, start=1):
            if i == selected:
                opt.configure(fg_color="#E2E037", bg_color="#E2E037", text_color="black")
            else:
                opt.configure(fg_color="#62c370", bg_color="#62c370", text_color="white")

quiz_instance = QuizStart(root)
root.mainloop()