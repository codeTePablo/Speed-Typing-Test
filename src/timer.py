import time
class Timer:
   def __init__(self):
      self.start_time = 0
      self.time_limit = 60

   def start(self):
      """ Starts the timer """
      # print the timer inside the label
      self.start_time = time.time()

   def stop():
      """ Stops the timer """
      pass

   def reset():
      """ Resets the timer """
      pass

   def get_time_remaining(self):
      """ Returns the time remaining """
      elapsed_time = time.time() - self.start_time
      time_remaining = max(0, self.time_limit - elapsed_time)
      return round(time_remaining)
