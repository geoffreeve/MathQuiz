import tkinter as tk


class TestFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        list_of_options = ["first option", "second option", "third option", "forth option"]
        first_option = tk.StringVar(self)
        first_option.set(list_of_options[0])

        tk.Label(self, text="Test Label 1").grid(row=0, column=0)
        tk.Entry(self, bd=5).grid(row=0, column=1)
        tk.Label(self, text="Test Label 2").grid(row=0, column=2)
        tk.Entry(self, bd=5).grid(row=0, column=3)
        tk.Label(self, text="Test check button 1").grid(row=2, column=0)
        tk.Checkbutton(self, bd=5).grid(row=2, column=1)
        tk.Label(self, text="Test check button 2").grid(row=2, column=2)
        tk.Checkbutton(self, bd=5).grid(row=2, column=3)
        tk.Label(self, text="Test drop down 1").grid(row=3, column=0)
        tk.OptionMenu(self, first_option, *list_of_options).grid(row=3, column=1)


class TestMainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test Application")

        for r in range(3):
            self.rowconfigure(r, weight=1)
        for c in range(8):
            self.columnconfigure(c, weight=1)

        self.testFrame1 = TestFrame()
        self.testFrame2 = TestFrame()
        self.testFrame3 = TestFrame()
        self.testFrame4 = TestFrame()
        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')
        self.testFrame2.grid(row=3, column=0, rowspan=3, columnspan=3, sticky='nsew')
        self.testFrame3.grid(row=0, column=3, rowspan=2, columnspan=3, sticky='nsew')
        self.testFrame3.grid(row=2, column=3, rowspan=4, columnspan=3, sticky='nsew')


TestMainApplication().mainloop()