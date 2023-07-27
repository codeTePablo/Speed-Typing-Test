import tkinter as tk
from word_generator import random_subject
import threading
import random
import time


class TypeSpeed:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Speed Typing Test")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        self.text = random_subject()

        self.frame = tk.Frame(self.root)

        self.label = tk.Label(
            self.frame, text=self.text, font=("Arial", 16), wraplength=400
        )
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Text(
            self.frame, width=50, height=10, font=("Arial", 16), wrap="word"
        )
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry.bind(
            "<KeyPress>", self.start
        )  #  when the user press a key, the start function will be called

        self.speed_label = tk.Label(
            self.frame, text="Speed: 0.00\nCPM: 0.00", font=("Arial", 16)
        )
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.frame.pack(expand=True)

        self.counter = 0
        self.errors = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in (16, 17, 18):
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.label.cget("text").startswith(self.input_entry.get("1.0", "end")):
            self.input_entry.config(fg="red")  #  wrong value
        else:
            self.input_entry.config(
                fg="black"
            )  #  change the color of the text to black
        if self.input_entry.get("1.0", "end") == self.label.cget("text")[:-1]:
            self.running = False  # stop the thread
            self.input_entry.config(fg="green")  #  correct value

            if self.input_entry.get("1.0", "end") == self.text[0]:
                self.text.pop(0)
                self.input_entry.delete(0, "end")
                self.label.config(text=" ".join(self.text))
            else:
                self.errors += 1
                self.input_entry.delete(0, "end")

    def time_thread(self):
        while self.running:
            time.sleep(1)
            self.counter += 1
            ops = (
                len(self.input_entry.get("1.0", "end")) / self.counter
            )  #  characters per second
            cpm = ops * 60  #  characters per minute
            self.speed_label.config(text=f"Speed: {ops:.2f}\nCPM: {cpm:.2f}")
            self.root.after(1000)

    def reset(self):
        self.counter = 0
        self.running = False
        self.speed_label.config(text="Speed: 0.00\nCPM: 0.00")
        self.text = random_subject()
        self.input_entry.delete(0, tk.END)


TypeSpeed()
