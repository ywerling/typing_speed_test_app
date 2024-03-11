import tkinter as tk
import time

TEXT_COLOR = 'black'
TEXT_FONT = 'arial.ttf'
TEXT_SIZE = 12

BENCHMARK_TEXT = ('All human beings are born free and equal in dignity and rights. They are endowed with reason and '
                  'conscience and should act towards one another in a spirit of brotherhood.')


class SpeedTypingApp(tk.Frame):
    """
        A class used to represent the UI of the Speed Typing Application
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
        self.start_time = None
        self.end_time = None


        # create the tkinter UI basic structure
        self.config(padx=800, pady=400)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # put widget on UI
        # self.canvas = tk.Canvas(width=200, height=150, bg="#666666", highlightthickness=0)
        # self.canvas.grid(row=2, column=1)

        self.instructions = tk.Label(self.parent,
                                           text="Type the text below:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.instructions.grid(row=0, column=0)

        self.text_benchmark = tk.Label(self.parent, text=BENCHMARK_TEXT, font=(TEXT_FONT, TEXT_SIZE), wraplength=200)
        self.text_benchmark.grid(row=1, column=0)

        self.type_label = tk.Label(self.parent, text="Enter in the yellow field below:", font=(TEXT_FONT, TEXT_SIZE), wraplength=200)
        self.type_label.grid(row=0, column=1)

        self.typing_entry = tk.Entry(self.parent, font=(TEXT_FONT, TEXT_SIZE), width=100, bg="#eee010")
        self.typing_entry.grid(row=1, column=1)
        self.typing_entry.bind("<Key>", self.start_timer)
        self.typing_entry.bind("<Return>", self.compute_speed)

        self.result_label = tk.Label(self.parent, text="Result", font=(TEXT_FONT, TEXT_SIZE))
        self.result_label.grid(row=2, column=1)

        self.instructions_label = tk.Label(self.parent, text="Start typing to start the timer and end with the return key", font=(TEXT_FONT, TEXT_SIZE), wraplength=200)
        self.instructions_label.grid(row=0, column=2)

    def start_timer(self, event):
        print("Start timer")
        if not self.start_time:
            self.start_time = time.time()

    def compute_speed(self, event):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        words_typed = len(self.typing_entry.get().split())
        speed = words_typed / (elapsed_time / 60)  # Calculate words per minute
        self.result_label.config(text=f"Your typing speed is {speed:.2f} words per minute.")
        self.typing_entry.config(state="disabled")  # Disable entry after calculation



# starts the UI in the main and keeps it open
if __name__ == "__main__":
    window = tk.Tk()
    window.title = "Speed Typing test Application"
    SpeedTypingApp(window)
    window.mainloop()
