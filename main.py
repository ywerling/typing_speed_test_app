import tkinter as tk


class SpeedTypingApp(tk.Frame):
    """
        A class used to represent the UI of the Image Watermarking Application
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Initializes the class
        :param parent:
        :param args:
        :param kwargs:
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create the tkinter UI basic structure
        self.config(padx=400, pady=300)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)

        # put widget on UI
        self.canvas = tk.Canvas(width=200, height=150, bg="#666666", highlightthickness=0)
        self.canvas.grid(row=1, column=1)



# starts the UI in the main and keeps it open
if __name__ == "__main__":
    window = tk.Tk()
    window.title="Image Watermarking Application"
    SpeedTypingApp(window)
    window.mainloop()
