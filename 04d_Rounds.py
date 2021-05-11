from tkinter import *
from functools import partial  # To prevent unwanted windows
import re

# This is the main GUI where the user selects their preferences and mode.
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
        self.rounds_button = Button(self.mode_frame, font='arial 12 bold', text="Rounds", padx=10, command=lambda:Start.error_checking(self, self.min_entry.get(), self.max_entry.get(), 1))
        self.rounds_button.grid(row=3, sticky="ew")
        # Unlimited button (row 4)
        self.unlimited_button = Button(self.mode_frame, font='arial 12 bold', text="Unlimited", padx=10)
        self.unlimited_button.grid(row=4, pady=5, sticky="ew")
        # Rounds button (row 5)
        self.Timer_button = Button(self.mode_frame, font='arial 12 bold', text="Timer", padx=10)
        self.Timer_button.grid(row=5, sticky="ew")

        # Instructions button (row 6)
        self.instructions_button = Button(self.mode_frame, font='arial 12 bold', text="Help/Instructions", padx=5)
        self.instructions_button.grid(row=6, pady=20)

    # This function is to check if the users entries (min/max num) are valid before going through with modes.
    def error_checking(self, min, max, mode):
        try:
            # Checks if the entry is blank. If it is, the user will get an error.
            if min == "" or max == "":
                self.error_label.config(text="One or more entries are blank.")
                return
            # If min or max is a string, it will attempt to change to a int. This will be caught by the try except and will print an error.
            min = int(min)
            max = int(max)
            # Checks if minimum number is higher than max number. If it is then user will get an error.
            if min > max:
                self.error_label.config(text="Min is higher than max, please enter a lower number")
                return
            # Checks if user has selected a radiobutton symbol, if not then the user will get an error.
            if self.symbol_selection.get() == 0:
                self.error_label.config(text="Please select a symbol.")
            # If there are no problems, the error label will reset and the program will proceed.
            else:
                self.error_label.config(text="")
                # If mode is 1, then the rounds class will be called.
                if mode == 1:
                    Rounds()

        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
        
        
# This is the rounds class which holds the rounds GUI if the user selects 'Rounds' in Start class
class Rounds:
    def __init__(self):
        # Creates new window called rounds_box
        self.rounds_box = Toplevel()
        # When this window is open, it disables any parent window until this one is closed.
        self.rounds_box.grab_set()
        # This force forces on the child window so that the user can't interact with the entry box once this window has been opened.
        self.rounds_box.focus_force()


        # If the user presses the X to exit, this will call a function which destroys the window and
        # recalls the Selection class.
        #self.rounds_box.protocol('WM_DELETE_WINDOW', self.close_rounds)

        # Main window frame
        self.rounds_frame = Frame(self.rounds_box, padx=20, pady=5)
        self.rounds_frame.grid()
        
        # Heading label (row 0)
        self.heading_label = Label(self.rounds_frame, text="Rounds", font='arial 30 bold')
        self.heading_label.grid(padx=10, pady=10)

        # Question label (row 1)
        self.question_label = Label(self.rounds_frame, text="How many rounds?", font='arial 15 italic')
        self.question_label.grid(row=1, pady=10)

        # Question entry (row 2)
        self.question_entry = Entry(self.rounds_frame)
        self.question_entry.grid(row=2)

        # Buttons frame
        self.buttons_frame = Frame(self.rounds_box)
        self.buttons_frame.grid()

        # Back button (row 3, column 0)
        self.back_button = Button(self.buttons_frame, text="Back", fg='white', bg='black', font='arial 12')
        self.back_button.grid(row=3, pady=10, padx=5)
        # Enter button (row 3, column 1)
        self.enter_button = Button(self.buttons_frame, text="Enter", fg='white', bg='black', font='arial 12')
        self.enter_button.grid(row=3, column=1)


class Math:
    def __init__(self):
        print("math class")

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.mainloop()
