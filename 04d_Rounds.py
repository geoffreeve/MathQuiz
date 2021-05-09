from tkinter import *
from functools import partial  # To prevent unwanted windows


class Start:
    def __init__(self, error=""):
        # Heading frame
        self.start_frame = Frame(padx=40, pady=15)
        self.start_frame.grid()

        # Heading label (row 0)
        self.heading_label = Label(self.start_frame, font='arial 24', text="Math quiz")
        self.heading_label.grid(row=0)

        # Hidden error label (row 0, Under heading label)
        self.error_label = Label(self.start_frame, text="", font='arial 12', fg='red', wraplength=150)
        self.error_label.grid()

        # If error variable has changed, then change the error label to the given error message.
        if error != "":
            self.error_label.configure(text=error)

        # Min frames
        self.min_max_frame = Frame(padx=10)
        self.min_max_frame.grid()
        # Min label (row 1, column 0)
        self.min_label = Label(self.min_max_frame, font='arial 12', text="Min number", justify=LEFT)
        self.min_label.grid(row=1, column=0)
        # Min slider (row 1, column 1)
        self.min_entry = Entry(self.min_max_frame, width=4, font='arial 14', )
        self.min_entry.grid(row=1, column=1)

        # Max label (row 2, column 0)
        self.max_label = Label(self.min_max_frame, font='arial 12', text="Max number", justify=LEFT)
        self.max_label.grid(row=2, column=0, pady=10, padx=10)
        # Max slider (row 2, column 1)
        self.min_entry = Entry(self.min_max_frame, font='arial 14', width=4)
        self.min_entry.grid(row=2, column=1)

        # Radio button frame
        self.radio_frame = Frame()
        self.radio_frame.grid()        

        # This variable changes depending on what radiobutton the user presses. These buttons are below.
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
        self.rounds_button = Button(self.mode_frame, font='arial 12 bold', text="Rounds", padx=10, command=lambda:Start.error_checking(self, min_entry.get(), max_entry.get()))
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
    def error_checking(self, min, max):
        try:
            # Check if min has any strings.
            for i in self.min:
                if i == str:
                    # If it does, then user will  be given an error.
                    Start.__init__(self, "Please enter a valid number.")
                else:
                    continue
            # If min num is higher than max num, then the user will be given an error.
            if self.min > self.max:
                Start.__init__(self, "Minimum number can't be higher than maximum number.")
            else:
                print("Working")
                Start.__init__(self, "")
        # If there is an error that cannot be specified, then the user will get a value error.
        except ValueError:
            print("!!!!!!!Something happened.!!!!!!")
        
        

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

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.mainloop()
