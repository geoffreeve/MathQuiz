from tkinter import *


# This class runs when the program starts and is the main window.
class Start:
    def __init__(self):
        # Heading frame
        self.start_frame = Frame(padx=40, pady=15)
        self.start_frame.grid()

        # Heading label (row 0)
        self.heading_label = Label(self.start_frame, font='arial 24', text="Math quiz")
        self.heading_label.grid(row=0)

        # Min frames
        self.min_max_frame = Frame(padx=10)
        self.min_max_frame.grid()
        # Min label (row 1, column 0)
        self.min_label = Label(self.min_max_frame, font='arial 12', text="Min number", justify=LEFT)
        self.min_label.grid(row=1, column=0)
        # Min slider (row 1, column 1)
        self.min_slider = Entry(self.min_max_frame, width=4, font='arial 14', )
        self.min_slider.grid(row=1, column=1)

        # Max label (row 2, column 0)
        self.max_label = Label(self.min_max_frame, font='arial 12', text="Max number", justify=LEFT)
        self.max_label.grid(row=2, column=0, pady=10, padx=10)
        # Max slider (row 2, column 1)
        self.min_slider = Entry(self.min_max_frame, font='arial 14', width=4)
        self.min_slider.grid(row=2, column=1)

        # Modes frame
        self.mode_frame = Frame(padx=5, pady=5)
        self.mode_frame.grid()
        # Mode label (row 1)
        self.mode_label = Label(self.mode_frame, font='arial 16 bold', text="Modes:")
        self.mode_label.grid(row=1, pady=10)
        # Rounds button (row 2)
        self.rounds_button = Button(self.mode_frame, font='arial 12 bold', text="Rounds", padx=10, command=lambda:Selection())
        self.rounds_button.grid(row=2, sticky="ew")
        # Unlimited button (row 3)
        self.unlimited_button = Button(self.mode_frame, font='arial 12 bold', text="Unlimited", padx=10)
        self.unlimited_button.grid(row=3, pady=5, sticky="ew")
        # Rounds button (row 4)
        self.Timer_button = Button(self.mode_frame, font='arial 12 bold', text="Timer", padx=10)
        self.Timer_button.grid(row=4, sticky="ew")

        # Instructions button
        self.instructions_button = Button(self.mode_frame, font='arial 12 bold', text="Help/Instructions", padx=5,
                                            command=self.to_help)
        self.instructions_button.grid(row=5, pady=20)

    def to_help(self):
        self.instructions_button.config(state=DISABLED)
        #Help(self)


class Selection():
    def __init__(self):
        # Main window frame
        self.selection_frame = Frame()
        self.selection_frame.grid()

        # Main heading label
        self.heading_label = Label(self.selection_frame, text="Selection", font='arial 30 bold')
        self.heading_label.grid()



# Rounds class
class Rounds:
    def __init__(self):
        # Main window frame
        self.rounds_frame = Frame(padx=20, pady=5)
        self.rounds_frame.grid()

        # Heading label (row 1)
        self.heading_label = Label(self.rounds_frame, text="Rounds", font='arial 30 bold')
        self.heading_label.grid(padx=10, pady=10)

        # Question label (row 2)
        self.question_label = Label(self.rounds_frame, text="How many rounds?", font='arial 15 italic')
        self.question_label.grid(row=2, pady=10)

        # Question entry (row 3)
        self.question_entry = Entry(self.rounds_frame)
        self.question_entry.grid(row=3)

        # Buttons frame
        self.buttons_frame = Frame()
        self.buttons_frame.grid()

        # Back button
        self.back_button = Button(self.buttons_frame, text="Back", fg='white', bg='grey', font='arial 12')
        self.back_button.grid(row=4, pady=10, padx=5)
        # Enter button
        self.enter_button = Button(self.buttons_frame, text="Enter", fg='white', bg='grey', font='arial 12')
        self.enter_button.grid(row=4, column=1)





# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.mainloop()
