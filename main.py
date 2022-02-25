import tkinter as tk
import logging
import datetime

from styling import *
root = tk.Tk()
logger = logging.getLogger()
a = (datetime.datetime.now())
print(a)

logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asc time)s % (level name)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.info("")

root.mainloop()
