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
names = [] #Stores the User's name
asked = [] #Questions that have been asked already
question_order = [] #Stores the order of questions that have been asked
selections = {} #Stores the answers the user have selected, without this, the code cannot remember
current_index = 0 #
score = 0
qnum = 0 #
total_questions = 10 #Total number of questions, allows me to edit code easily

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
font_path = Path(__file__).parent / 'fonts/BalsamiqSans-Regular.ttf' # Specifies which font I will use
pyglet.options['win32_gdi_font'] = True # Registers font with Windows Operating System and improves compatibility
pyglet.font.add_file(str(font_path)) # Adds font file into Tkinter using the variable set above
balsamiqsans = "Balsamiq Sans" # Registers family name of the font as a variable

#Fonts for Start-Up Page
main_font=ctk.CTkFont(family=balsamiqsans, size=50, weight="bold") # Let's Start button
exit_font=ctk.CTkFont(family=balsamiqsans, size=25) # Exit button in Start-Up page
entry_font_title=ctk.CTkFont(family=balsamiqsans, size=18) # "Please enter your name!" above the entry
entry_font=ctk.CTkFont(family=balsamiqsans, size=14) # Inputted text for the user's name in the entry

#Fonts for Quiz, Answer Feedback, and Result Page
answer_font=ctk.CTkFont(family=balsamiqsans, size=28, weight="bold") # Multiple choice radiobuttons for bird options
main_exit_font=ctk.CTkFont(family=balsamiqsans, size=27) # Exit button in Quiz, Answer Feedback, and Result page
secondary_font=ctk.CTkFont(family=balsamiqsans, size=20) # Previous, Submit, Next, and Continue Buttons
questionnumber_font=ctk.CTkFont(family=balsamiqsans, size=32, weight="bold") # Question counter

result_font=ctk.CTkFont(family=balsamiqsans, size=60, weight="bold") # Correct!/Incorrect in Answer Feedback page, and text in the Result page.

# Adjust size of windows
root.geometry("1280x720") # Specifies that the window size will be 1280 x 720

#
# DEFINED FUNCTIONS
#

# Close Window
def close_window():
    root.destroy() # Closes the program

def randomiser():
    # Selects a random question that hasn't been asked yet
    global qnum
    qnum = random.randint(1, len(questions_answers))
    if qnum not in asked:
        asked.append(qnum)
    else:
        randomiser()

#
# SCREEN 1 - Start-Up Page
#
class QuizStart:
    def __init__(self, parent):
        self.parent = parent
        # Create Frame
        self.frame=Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)
        # Display the background
        bg = PIL.Image.open("images/homepage.png") # Allows CustomTkinter to recognise the background I have uploaded to use the CtkImage function
        bg_image=ctk.CTkImage(light_image=bg,dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Name Input Entry
        self.entrylabel = ctk.CTkLabel(self.frame, font=entry_font_title, text="Please enter your name!", fg_color="white") # Entry label for users to input their name
        self.entrylabel.place(x=550, y=403)
        self.entryname = Entry(self.frame, font=entry_font, relief="solid")
        self.entryname.place(x=570, y=443)
        # Adding Start and Exit Button
        self.button1=ctk.CTkButton(self.frame, text="Let's Start",
                                   bg_color="white", fg_color="#62c370", font=main_font, text_color="white",
                                   width=322, height=100, corner_radius=50, command=self.start_quiz) # Let's Start button that starts the quiz
        self.button2=ctk.CTkButton(self.frame, text="Exit",
                                   bg_color="#e46a4a", fg_color="white", font=exit_font, text_color="black",
                                   width=100, height=18, corner_radius=8, command=close_window) # Exit button that closes the quiz
        # Display "Let's Start" Button
        self.button1.place(x=479, y=582, anchor="sw")
        # Display "Exit" Button
        self.button2.place(x=1152, y=72, anchor="sw")
    # Function to Start the Quiz
    def start_quiz(self):
        name = self.entryname.get().strip()
        if name.isdigit(): # Checks if the name is only just numbers, then makes user retry
            messagebox.showerror("Error", "You cannot have numbers in your name.")
        elif name: # If there is a name, lets user proceed through quiz
            names.append(name)
            self.frame.destroy()
            Quiz(self.parent)
        else: # If the name is blank, then makes user retry
            messagebox.showerror("Error", "Your name cannot be blank. Please enter your name.")

#
# SCREEN 2 - Main Quiz Page
#
class Quiz:
    def __init__(self, parent):
        self.parent = parent
        global qnum
        # Pick a new question only if navigating forward into unseen questions
        if current_index >= len(question_order):
            randomiser()
            question_order.append(qnum)
        else:
            qnum = question_order[current_index]
        # Create Frame
        self.frame=Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)
        # Display the background
        # Adding background images
        bg = PIL.Image.open(questions_answers[qnum][7]) # Allows CustomTkinter to recognise the background I have uploaded to use the CtkImage function
        bg_image=ctk.CTkImage(light_image=bg,dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Adding Question Count
        self.questioncounter = ctk.CTkLabel(self.frame, text=f"{current_index + 1}/{total_questions}", font=questionnumber_font, fg_color="#62c370",
                                            text_color="white") # Gives the user the position of the quiz they are at
        self.questioncounter.place(x=120, y=120)
        # Adding Exit Button
        self.button2=ctk.CTkButton(self.frame, text="Exit",
                                   bg_color="#e46a4a", fg_color="white", font=main_exit_font, text_color="black",
                                   width=94, height=14, corner_radius=7, command=close_window) # Exit button that closes the quiz
        # Display "Exit" Button
        self.button2.place(x=1080, y=153, anchor="sw")

        self.var = IntVar(value=selections.get(qnum, 0))
        self.var.trace_add("write", lambda *_: self.update_submit_state())

        # Adding Answer Option Buttons
        self.option1 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][1],
                    variable=self.var, value=1, width=180, height=1,
                    font=answer_font, hover_color="white",
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option1.place(x=109, y=257) # Answer Option 1

        self.option2 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][2],
                    variable=self.var, value=2, width=180, height=1,
                    font=answer_font, hover_color="white",
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option2.place(x=956, y=257) # Answer Option 2

        self.option3 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][3],
                    variable=self.var, value=3, width=180, height=1,
                    font=answer_font, hover_color="white",
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option3.place(x=109, y=470) # Answer Option 3

        self.option4 = ctk.CTkRadioButton(self.frame,
                    text=questions_answers[qnum][4],
                    variable=self.var, value=4, width=180, height=1,
                    font=answer_font, hover_color="white",
                    fg_color="#62c370", text_color="white", bg_color="#62c370",
                    command=self.highlight_selected)
        self.option4.place(x=956, y=470) # Answer Option 4

        is_last = current_index >= total_questions - 1 # Defines a variable that checks whether the current question is the last question

        # Previous Button
        self.prev_button = ctk.CTkButton(self.frame, text="Previous",
                                         bg_color="#ff924d", fg_color="white", font=secondary_font, text_color="black",
                                         width=100, height=46, corner_radius=8,
                                         command=self.go_previous)
        self.prev_button.place(x=448, y=598, anchor="center")

        # Next (Skip) Button
        self.next_button = ctk.CTkButton(self.frame, text="Next",
                                         bg_color="white", fg_color="white", font=secondary_font, text_color="black",
                                         width=94, height=14, corner_radius=7,
                                         command=self.go_next)
        self.next_button.place(x=836, y=598, anchor="center")

        # Submit Button
        self.submit_button = ctk.CTkButton(self.frame, text="Submit",
                                           bg_color="white", fg_color="white", font=secondary_font, text_color="black",
                                           width=94, height=14, corner_radius=7,
                                           command=self.submit_answer)
        self.submit_button.place(x=643, y=598, anchor="center")

        if current_index == 0: # Disables the previous button if it is the first question
            self.prev_button.configure(state="disabled")
        if is_last: # Disables the last button if it is the last question
            self.next_button.configure(state="disabled")
        self.update_submit_state()
        # Re-apply highlight if user had previously selected an answer
        if self.var.get() != 0:
            self.highlight_selected()

    def update_submit_state(self):
        if self.var.get() == 0:
            self.submit_button.configure(state="disabled") # When the user hasn't selected an answer, disables the submit button
        else:
            self.submit_button.configure(state="normal") # Enables the submit button if an answer is selected
            self.next_button.configure(state="disabled") # Disables the next button if an answer is selected

    # Function to return to the previous question
    def go_previous(self):
        global current_index
        selections[qnum] = self.var.get()
        if current_index > 0:
            current_index -= 1
            self.frame.destroy()
            Quiz(self.parent)

    # Function to skip to the next question
    def go_next(self):
        global current_index
        selections[qnum] = self.var.get()
        if current_index < total_questions - 1:
            current_index += 1
            self.frame.destroy()
            Quiz(self.parent)

    # Function to submit an answer, checking whether it is correct or incorrect, then makes user proceed to answer feedback page
    def submit_answer(self):
        if self.var.get() == 0:
            return
        selections[qnum] = self.var.get()
        is_correct = self.var.get() == questions_answers[qnum][6]
        self.frame.destroy()
        AnswerScreen(self.parent, qnum, is_correct)

    def highlight_selected(self): # Function that highlights what the user has selected as an answer
        options = [self.option1, self.option2, self.option3, self.option4]
        selected = self.var.get()
        for i, opt in enumerate(options, start=1):
            if i == selected:
                opt.configure(fg_color="#E2E037", bg_color="#E2E037", text_color="black")
            else:
                opt.configure(fg_color="#62c370", bg_color="#62c370", text_color="white")

#
# SCREEN 3 - Answer Feedback Page (Correct/Incorrect)
#
class AnswerScreen:
    def __init__(self, parent, question_num, is_correct):
        self.parent = parent
        self.frame = Frame(parent, width=1280, height=720)
        self.frame.pack(fill="both", expand=True)

        # Background derived from the question's bird image
        bird_name = Path(questions_answers[question_num][7]).stem
        bg = PIL.Image.open(f"images/answers/{bird_name}_answer.png") # Allows CustomTkinter to recognise the background I have uploaded to use the CtkImage function
        bg_image = ctk.CTkImage(light_image=bg, dark_image=bg, size=(1280, 720))
        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Question counter
        self.questioncounter = ctk.CTkLabel(self.frame, text=f"{current_index + 1}/{total_questions}", font=questionnumber_font, fg_color="#62c370",
                                            text_color="white")
        self.questioncounter.place(x=120, y=120)

        # Exit button
        self.exit_button = ctk.CTkButton(self.frame, text="Exit",
                                         bg_color="#e46a4a", fg_color="white", font=main_exit_font, text_color="black",
                                         width=94, height=14, corner_radius=7, command=close_window) # Exit button that closes the quiz
        self.exit_button.place(x=1080, y=153, anchor="sw")

        # Correct / Incorrect text with 200px padding from top, centered horizontally
        text = "Correct!" if is_correct else "Incorrect"
        colour = "#62c370" if is_correct else "#e46a4a"
        self.result_label = ctk.CTkLabel(self.frame, text=text, font=result_font,
                                         text_color=colour, fg_color="white")
        self.result_label.place(x=640, y=75, anchor="n")

        # Continue button
        self.continue_button = ctk.CTkButton(self.frame, text="Continue",
                                             bg_color="white", fg_color="white", font=secondary_font, text_color="black",
                                             width=94, height=16, corner_radius=8,
                                             command=self.go_on)
        self.continue_button.place(x=643, y=598, anchor="center")

    # Goes to the next question, if this is the last question, gives user a final score
    def go_on(self):
        global current_index, score
        if current_index >= total_questions - 1:
            score = sum(1 for q, ans in selections.items() if ans == questions_answers[q][6])
            messagebox.showinfo("Quiz Complete", f"{names[-1]}, you scored {score}/{total_questions}!")
            close_window()
        else:
            current_index += 1
            self.frame.destroy()
            Quiz(self.parent)

root.title("New Zealand Native Bird Quiz")
quiz_instance = QuizStart(root)
root.resizable(0, 0)
root.mainloop()