from tkinter import *


class Start:
    def __init__(self):
        # Heading frame
        self.start_frame = Frame(padx=50, pady=15)
        self.start_frame.grid()

        # Heading label (row 0)
        self.heading_label = Label(self.start_frame, font='arial 24', text="Math quiz")
        self.heading_label.grid(row=0)

        # Min Max frames ()
        self.min_max_frame = Frame()
        self.min_max_frame.grid()
        # Min label (row 1)
        self.min_label = Label(self.min_max_frame, font='arial 12', text="Min number", justify=LEFT)
        self.min_label.grid(row=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    something = Start()
    root.mainloop()
