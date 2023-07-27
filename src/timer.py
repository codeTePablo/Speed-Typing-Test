import time
import math
from tkinter import * 
from window import canvas, root, timer_text, title_label

time = 60
timer = None

def start_timer(count):
   """ start the timer """
   count_min = math.floor(count/60) # return min 
   count_sec = count % 60 # result the result of sec 
   if count_sec == 10:
      count_sec = f"0:{count_sec}" 
   # print(count_sec)

   canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}" )


def reset(): 
   root.after_cancel(timer)
   canvas.config(timer_text, text="00:00")
   title_label.config(text="Timer")

# CREAR EL GIT INGNORE