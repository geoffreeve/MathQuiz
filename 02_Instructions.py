from tkinter import *


class Start:
    def __init__(self):
        # Heading frame
        self.start_frame = Frame(padx=30, pady=15)
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
        self.min_slider = Scale(self.min_max_frame, from_=1, to=50, orient=HORIZONTAL, length=150)
        self.min_slider.grid(row=1, column=1)

        # Max label (row 2, column 0)
        self.max_label = Label(self.min_max_frame, font='arial 12', text="Max number", justify=LEFT)
        self.max_label.grid(row=2, column=0)
        # Max slider (row 2, column 1)
        self.min_slider = Scale(self.min_max_frame, from_=1, to=100, orient=HORIZONTAL, length=150)
        self.min_slider.grid(row=2, column=1)

        # Modes frame
        self.mode_frame = Frame(padx=5, pady=5)
        self.mode_frame.grid()
        # Mode label (row 1)
        self.mode_label = Label(self.mode_frame, font='arial 16 bold', text="Modes:")
        self.mode_label.grid(row=1, pady=10)
        # Rounds button (row 2)
        self.rounds_button = Button(self.mode_frame, font='arial 12 bold', text="Rounds", padx=10)
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
        Help(self)
        


class Help:
    def __init__(self, partner):
        # Create new window
        box = Toplevel()

        # Help frame
        self.help_frame = Frame(box, padx=10, pady=10)
        self.help_frame.grid()

        # Header label (row 0)
        self.header_label = Label(self.help_frame, font='arial 16', text="Help / Instructions")
        self.header_label.grid(row=0, pady=5)

        # Help text label (row 1)
        self.help_label = Label(self.help_frame, font='arial 12', text="Help text goes here...")
        self.help_label.grid(row=1, pady=5)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, font='arial 12', text="Dismiss",
                                    command=lambda: self.close_help(partner))
        self.dismiss_button.grid(row=2, pady=5)

    def close_help(self, partner):
        partner.instructions_button.config(state=NORMAL)
        partner.box.destroy()



# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.mainloop()
