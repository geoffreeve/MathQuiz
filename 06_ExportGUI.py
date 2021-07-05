from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random

# This is the main GUI where the user enters their preferred settings and mode.
# If the users input is valid and they click a mode, it should go ahead with that specific mode.
class Start:
    def __init__(self, error=""):
        # Heading frame
        self.start_frame = Frame(padx=40, pady=15)
        self.start_frame.grid()

        # Heading label (row 0)
        self.heading_label = Label(self.start_frame, font='arial 24', text="Math quiz")
        self.heading_label.grid(row=0)

        # Hidden error label (row 0, Under Heading label)
        self.error_label = Label(self.start_frame, text="", font='arial 12', fg='red', wraplength=150)
        self.error_label.grid()

        # If error variable has changed, then there is an error.
        # This will change the error label from blank and print the error.
        if error != "":
            self.error_label.configure(text=error)

        # Min/Max frames
        self.min_max_frame = Frame(padx=10)
        self.min_max_frame.grid()
        # Min label (row 1, column 0)
        self.min_label = Label(self.min_max_frame, font='arial 12', text="Min number", justify=LEFT)
        self.min_label.grid(row=1, column=0)
        # Min Entry (row 1, column 1)
        self.min_entry = Entry(self.min_max_frame, width=4, font='arial 14')
        self.min_entry.grid(row=1, column=1)

        # Max label (row 2, column 0)
        self.max_label = Label(self.min_max_frame, font='arial 12', text="Max number", justify=LEFT)
        self.max_label.grid(row=2, column=0, pady=10, padx=10)
        # Max Entry (row 2, column 1)
        self.max_entry = Entry(self.min_max_frame, font='arial 14', width=4)
        self.max_entry.grid(row=2, column=1)

        # Radio button frame
        self.radio_frame = Frame()
        self.radio_frame.grid()        

        # This variable is linked to the radiobuttons and will change depending on which button the user selects.
        self.symbol_selection = IntVar()

        # Radio buttons
        # Addition button(row 1, column 0)
        self.addition_radio_button = Radiobutton(self.radio_frame, text="+", font='arial 12 bold', variable=self.symbol_selection, value=1)
        self.addition_radio_button.grid(row=1, column=0)
        # Subtraction button (row 1, column 1)
        self.subtract_radio_button = Radiobutton(self.radio_frame, text="-", font='arial 12 bold', variable=self.symbol_selection, value=2)
        self.subtract_radio_button.grid(row=1, column=1)
        # Multiplication button (row 1, column 2)
        self.multiplication_radio_button = Radiobutton(self.radio_frame, text="x", font='arial 12 bold', variable=self.symbol_selection, value=3)
        self.multiplication_radio_button.grid(row=1, column=2)
        # Division button (row 1, column 3)
        self.division_radio_button = Radiobutton(self.radio_frame, text="/", font='arial 12 bold', variable=self.symbol_selection, value=4)
        self.division_radio_button.grid(row=1, column=3)

        # Modes frame
        self.mode_frame = Frame(padx=5, pady=5)
        self.mode_frame.grid()
        # Mode label (row 2)
        self.mode_label = Label(self.mode_frame, font='arial 16 bold', text="Modes:")
        self.mode_label.grid(row=2, pady=10)
        # Rounds button (row 3)
        
        self.rounds_button = Button(self.mode_frame, font='arial 12 bold', text="Rounds", padx=10, command=lambda:Start.error_checking(self, 1))
        self.rounds_button.grid(row=3, sticky="ew")
        # Unlimited button (row 4)
        self.unlimited_button = Button(self.mode_frame, font='arial 12 bold', text="Unlimited", padx=10, command=lambda:Start.error_checking(self, 2))
        self.unlimited_button.grid(row=4, pady=5, sticky="ew")
        # Rounds button (row 5)
        self.Timer_button = Button(self.mode_frame, font='arial 12 bold', text="Timer", padx=10)
        self.Timer_button.grid(row=5, sticky="ew")

        # Instructions button (row 6)
        self.instructions_button = Button(self.mode_frame, font='arial 12 bold', text="Help/Instructions", padx=5)
        self.instructions_button.grid(row=6, pady=20)

    # This function is to check if the users entries (min/max num) are valid before going through with modes.
    def error_checking(self, mode):
        try:
            # This sets the minimum value and maximum value, based on what the user enters in the entry box.
            min = self.min_entry.get()
            max = self.max_entry.get()
            # Checks if the entry is blank. If it is, the user will get an error.
            if min == "" or max == "":
                self.error_label.config(text="One or more entries are blank.")
                return
            # If min or max is a string, it will attempt to change to a int. This will be caught by the try except and will print an error.
            min = int(min)
            max = int(max)
            # Checks if user has entered a min number higher than 0.
            if min <= 0:
                self.error_label.config(text="Enter a number higher than 0.")
                return
            # Checks if minimum number is higher than max number. If it is then user will get an error.
            if min > max:
                self.error_label.config(text="Min is higher than max, please enter a lower number")
                return
            # Checks if user has selected a radiobutton symbol, if not then the user will get an error.
            if self.symbol_selection.get() == 0:
                self.error_label.config(text="Select a symbol.")
            # If there are no problems, the error label will reset and the program will proceed.
            else:
                self.error_label.config(text="")
                # If mode is 1, then the rounds class will be called.
                if mode == 1:
                    Rounds(self.symbol_selection.get(), int(self.min_entry.get()), int(self.max_entry.get()))
                elif mode == 2:
                    Modes(self.symbol_selection.get(), int(self.min_entry.get()), int(self.max_entry.get()), 0, mode)

        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
        
        
# This Rounds class is a dedicated window for ROUNDS mode.
# It will ask the user how many rounds they want to play.
class Rounds:
    def __init__(self, symbol, min, max):
        # Creates new window called rounds_box
        self.rounds_box = Toplevel()
        # When this window is open, it disables any parent window until this one is closed.
        self.rounds_box.grab_set()
        # This force forces on the child window so that the user can't interact with the entry box once this window has been opened.
        self.rounds_box.focus_force()

        # If the user presses the X to exit, this will call a function which destroys the window and
        # recalls the Selection class.
        self.rounds_box.protocol('WM_DELETE_WINDOW', self.rounds_quit)

        # Main window frame
        self.rounds_frame = Frame(self.rounds_box, padx=20, pady=5)
        self.rounds_frame.grid()
        
        # Heading label (row 0)
        self.heading_label = Label(self.rounds_frame, text="Rounds", font='arial 30 bold')
        self.heading_label.grid(padx=10, pady=10)

        # Question label (row 1)
        self.question_label = Label(self.rounds_frame, text="How many rounds?", font='arial 15 italic')
        self.question_label.grid(row=1)

        # Hidden error label (row 2)
        self.error_label = Label(self.rounds_frame, text="", font='arial 12', fg='red', wraplength=150)
        self.error_label.grid(row=2, pady=10)

        # Question entry (row 3)
        self.question_entry = Entry(self.rounds_frame)
        self.question_entry.grid(row=3)

        # Buttons frame
        self.buttons_frame = Frame(self.rounds_box)
        self.buttons_frame.grid()

        # Back button (row 4, column 0)
        self.back_button = Button(self.buttons_frame, text="Back", fg='white', bg='black', font='arial 12', command=lambda: self.rounds_quit())
        self.back_button.grid(row=4, pady=10, padx=5)
        # Enter button (row 4, column 1)
        self.enter_button = Button(self.buttons_frame, text="Enter", fg='white', bg='black', font='arial 12', command=lambda: self.rounds_go(symbol, min, max, self.question_entry.get()))
        self.enter_button.grid(row=4, column=1)

    # Used to exit rounds window. This is if the user decides they don't want to play rounds anymore.
    def rounds_quit(self):
        self.rounds_box.destroy()
    # This function will check if the user has entered a valid number for rounds. If they have then it will
    # Call the 'Modes' class which is where the game will begin.
    def rounds_go(self, symbol, min, max, rounds):
        try:
            # If int(rounds) creates an error, this means the user did not enter a number.
            rounds = int(rounds)
            # Checks if the user entered a number higher than 0.
            if rounds <= 0:
                self.error_label.config(text="Please enter a number higher than 0")
            # If the users input is valid, the rounds window will be destroyed and 'Modes' class will be called.
            else:
                self.rounds_box.destroy()
                Modes(symbol, min, max, rounds+1, 1)
        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
        
        
# This class is as a dedicated window to display the main quiz for UNLIMITED and ROUNDS mode.
# It will ask the user questions depending on the settings the user previously set.
class Modes:
    # Parameters: MODE- Check if user is playing rounds or unlimited mode. || SYMBOL- Its the symbol which the user selected in previous windows (+ - / *) ||
    # MIN, MAX- The minimum and maximum number range that the user entered in previous windows.
    def __init__(self, symbol, min, max, rounds, mode):
        # Creates new window
        self.Modes_box = Toplevel()
        # When this window is open, it disables any parent window until this one is closed.
        self.Modes_box.grab_set()
        # This force forces on the child window so that the user can't interact with the entry box once this window has been opened.
        self.Modes_box.focus_force()

        # These IntVar's hold relevant variables that are used and set through multiple different functions.
        self.eqn_ans = IntVar()
        self.question = StringVar()
        self.rounds = IntVar()
        self.symbol = IntVar()
        self.mode = IntVar()


        self.question_arr = []
        self.answer_arr = []
        self.user_answer_arr = []
        
        self.rounds.set(rounds)
        self.symbol.set(symbol)
        self.mode.set(mode)

        # Top frame
        self.Modes_frame = Frame(self.Modes_box)
        self.Modes_frame.grid(padx=30, pady=20)

        # Heading label (row 0)
        self.heading_label = Label(self.Modes_frame, text="Heading", font='arial 24')
        self.heading_label.grid(row=0)

        
        # Error label (row 3)
        self.error_label = Label(self.Modes_frame, text="", font='arial 13', fg="red", wraplength=150)
        self.error_label.grid(row=1)

        # Question label (row 2)
        self.question_label = Label(self.Modes_frame, text="Question here", font='arial 15')
        self.question_label.grid(row=2)

        # Answer label (row 1)
        self.answer_label = Label(self.Modes_frame, text="", font='arial 12 bold')
        self.answer_label.grid(row=3)

        # Answer entry (row 4)
        self.answer_entry = Entry(self.Modes_frame, width=13)
        self.answer_entry.grid(row=4)

        # Buttons frame
        self.buttons_frame = Frame(self.Modes_box)
        self.buttons_frame.grid(padx=5, pady=5)
    
        # Back button (row 0, column 0)
        self.back_button = Button(self.buttons_frame, text="Back", font='arial 12', fg='white', bg='black', command=lambda:Modes.exit_modes(self, mode))
        self.back_button.grid(row=0, column=0)
        # Enter button (row 0, column 1)
        self.enter_button = Button(self.buttons_frame, text="Enter", font='arial 12', fg='white', bg='black', command=lambda:Modes.error_checking(self, self.answer_entry.get(), self.eqn_ans.get()))
        self.enter_button.grid(row=0, column=1, padx=5)
        # Next button frame
        self.next_button_frame = Frame(self.Modes_box)
        self.next_button_frame.grid(pady=5)
        # Next button (row 1)
        self.next_button = Button(self.next_button_frame, text="Next", font='arial 12', fg='white', bg='black', padx=10, command=lambda:Modes.next_func(self, symbol, min, max))
        self.next_button.grid(row=1)
        
        Modes.equations(self, symbol, min, max)

    # This function is used to exit the 'modes' GUI
    def exit_modes(self, mode):
        # Open Export window if user exits unlimited mode with more than 1 round played.
        if mode == 2:
            if len(self.user_answer_arr) > 1:
                Export(self.question_arr, self.user_answer_arr, self.answer_arr)
        self.Modes_box.destroy()

    # This function is used for the next button. It will check for skips and add values to the game history.
    def next_func(self, symbol, min, max):
        # If user entry is blank and they click next, the game history will record 'skipped'
        if self.answer_entry.get() == "":
            print("skiippped")
            print("Answer here: {}".format(self.answer_entry.get()))
            self.user_answer_arr.append("Skipped")
        # Appends the answer and question to game history.
        self.answer_arr.append(self.eqn_ans.get())
        self.question_arr.append(self.question.get())
        # Reset Enter button to normal.
        self.enter_button.config(state=NORMAL)
        Modes.equations(self, symbol, min, max)

    # This function changes the labels for Mode class, depending on which mode the user plays.
    # (EXAMPLE: If user is playing rounds mode, the heading will change to rounds;
    #  If user is playing unlimited mode, the heading will change to unlimited.)
    def GUI(self, question, mode):
        # If user selected rounds mode..
        if mode == 1:
            # If user runs out of rounds..
            if self.rounds.get() == 0:
                # Destroy the quiz window.
                self.Modes_box.destroy()
                Export(self.question_arr, self.user_answer_arr, self.answer_arr)
                return
            # If user hasn't run out of rounds..
            else:
                # Changes heading to rounds + amount of rounds left.    
                self.heading_label.config(text="Rounds: {}".format(self.rounds.get()))
        # If user selected unlimited mode..
        else:
            # Changes heading to Unlimited
            self.heading_label.config(text="Unlimited")
        # This line of code below assigns the 'question' string to 'answer', but removes the last item as shown below.
        # 'x + y =' ---> 'x + y'
        self.question_label.config(text=question)
        self.answer_label.config(text="")


    # Parameters: OPTION- Checks which symbol the user selected. || MIN, MAX- The minimum and maximum number range which was given by user in previous windows.
    # This function creates equation and returns them.
    def equations(self, symbol, min, max):
        symbol_list = ["+", "-", "*", "/"]
        # Generate two numbers within range.
        a = random.randint(min, max)
        b = random.randint(min, max)

        # If user is playing with division, use the following code to prevent breaking.
        if symbol == 4:
            c = random.randint(min, max)
            a = c * b

        question = "{} {} {} =".format(a, symbol_list[symbol-1], b)
        answer = question[:-1]
        # Eval function then takes the 'answer' string which should be "x + y" and converts and reads it as a int question
        # The Eval function will add it up and assign its output to answer.
        answer = int(eval(answer))
        self.eqn_ans.set(answer)
        self.question.set(question)
        # Once a question and answer is generated, this is stored in the following arrays.
        # This will be used in the Export class later.
        self.answer_entry.config(state=NORMAL)
        self.answer_entry.delete(0, 'end')
        if self.mode.get() == 1:
            new_rounds = self.rounds.get()
            new_rounds-=1
            self.rounds.set(new_rounds)
            Modes.GUI(self, question, self.mode.get())
        # If mode is unlimited mode, call GUI function without changing any variables/labels.
        else:
            Modes.GUI(self, question, self.mode.get())
            

    # Check if users response to question is valid, then checks if it is correct or incorrect.
    def error_checking(self, response, answer):
        try:
            # Checks if response is blank.
            if str(response) == "":
                self.error_label.config(text="Please enter a number.")
                return
            self.error_label.config(text="")
            # Checks if users response(answer) is equal to the program answer.
            if int(response) == self.eqn_ans.get():
                # If it is, answer label will change to:
                self.answer_label.config(text="Correct", fg='green')
            else:
                self.answer_label.config(text="Incorrect.\nAnswer: {}".format(answer), fg='red')
            # If there are no errors, the entry box and enter button will grey out so that the user cannot edit their answer.
            print("Here")
            self.answer_entry.config(state=DISABLED)
            self.enter_button.config(state=DISABLED)
            # This adds the users answer, whether correct or incorrect, into this array. 
            # It will be used later in Export class.
            self.user_answer_arr.append(response)
            
        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
            print("STILWORKINMG!!!!!!!!!!!!")
            print(self.user_answer_arr)
        

# Export class is used to export the users game history after they are done with a mode.
class Export:
    def __init__(self, question, user_answer, answer):

        # Sets up child window (export box)
        self.export_box = Toplevel()
        # Setup GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Setup export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Calculation export", font="arial 19 bold")
        self.how_heading.grid(row=0)

        # export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file.", justify=LEFT,
                                 width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history", justify=LEFT,
                                 bg='#ffafaf', fg="maroon", font="arial 10 italic",
                                 wrap=225, padx=10, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=lambda: self.save_history(question, user_answer, answer))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=lambda:(self.export_quit()))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, question, user_answer, answer):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = 'no'

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "No spaces allowed."
            else:
                problem = ("No {}'s allowed.".format(letter))
            has_error = "yes"
            break
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
        else:
            # If there are no errors, generate text file and then close dialogue
            # Add .txt suffix!
            filename = filename + ".txt"

            # Create file to hold data
            print(filename)
            f = open(filename, "w+")

            print("Question: {}".format(question))
            print("Answer: {}".format(answer))
            print("user-answer: {}".format(user_answer))

            # Add new line at end of each item
            for i in range(0, len(question)):
                f.write("Question: {} {} || Your Answer: {}\n".format(question[i], answer[i], user_answer[i]))
            
            # Close file
            f.close()

            # Close dialogue
            self.export_quit()
        
    def export_quit(self):
        self.export_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.resizable(False, False)
    root.mainloop()
