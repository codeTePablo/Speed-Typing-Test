import tkinter as tk
from word_generator import random_subject
# from timer import Timer.start

class SpeedTypingTest:

   def __init__(self):
         # self.timer = Timer()
         # self.root = Tk()
         # self.time_label = Label(self.root, text="Time remaining: ")
         # self.time_label.pack()
         pass

   def main():
      """ show the main window """
      # create the main window
      root = tk.Tk()
      root.title("Speed Typing Test")
      root.geometry("800x600")
      # resizable adapt the window size to the widgets inside
      root.resizable(False, False)

      # change the color of main window
      root.config(bg="#02A5F2")

      # create a freame for the text generated
      text_frame = tk.Frame(root, width=600, height=400)
      text_frame.grid(row=0, column=0, padx=10, pady=10)
      # change color of the frame
      text_frame.config(bg="red")
      # create a label widget inside the frame without the 
      text_label = tk.Label(text_frame, text=random_subject(), font=("Arial", 16), width=50, height=10, wraplength=500, justify="center")
      text_label.grid(row=0, column=0, padx=10, pady=10)

      # create a frame for the text input
      input_frame = tk.Frame(root, width=600, height=100)
      input_frame.grid(row=1, column=0, padx=10, pady=10)
      input_frame.config(bg="blue")
      # create a text input widget inside the input frame
      input_text = tk.Text(input_frame, width=50, height=1, font=("Arial", 16), wrap="word")
      input_text.grid(row=1, column=0, padx=10, pady=10)
      
      # create a frame for the buttons
      button_frame = tk.Frame(root, width=600, height=100)
      button_frame.grid(row=2, column=0, padx=10, pady=10)
      button_frame.config(bg="green")

      # create a frame for the results
      results_frame = tk.Frame(root, width=200, height=600)
      results_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)
      results_frame.config(bg="yellow")
      # create a label widget with timer 1:00 and countdown 
      timer_label = tk.Label(results_frame, text=start(), font=("Arial", 14))
      timer_label.grid(row=0, column=0, padx=10, pady=10)

      root.mainloop()

def update_interface(self):
      time_remaining = self.timer.get_time_remaining()
      self.time_label.configure(text="Time remaining: {} seconds".format(time_remaining))
      self.root.after(1000, self.update_interface)  # Actualiza la interfaz cada segundo

