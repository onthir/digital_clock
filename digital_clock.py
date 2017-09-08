import time
import tkinter as tk
from tkinter import *

background_color = input("Enter a color (ALL CAPS) for background: ")
color = input("Enter text color")

def tick(time1 =''):
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

root = tk.Tk()
root.title("TIme")
clock_frame = tk.Label(root, font=('arial 100 bold'),bg = background_color, fg=color)
clock_frame.pack(fill='both', expand=1)
root.geometry('700x500')
root.configure(background="lightgreen")
tick()
root.mainloop()
    
