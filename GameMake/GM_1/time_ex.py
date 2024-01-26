from tkinter import *
from datetime import datetime
import time

t_0 = datetime.now()

while True:
    time.sleep(1)
    t_now = datetime.now()
    t_delta = (t_now - t_0).total_seconds()
    # print(round(t_delta))
    print(round(t_delta, 1))