import tkinter as tk
import time


# create function to get a time

def tick():
    time_string=time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    #call tick() after every 200  seconds  display new time
    clock.after(200,tick)
root=tk.Tk()
root.geometry("500x400")
root.title("Digital Analog Clock")


# create a label to display a window
clock=tk.Label(root,font=("time",100,"bold",),bg="orange")
clock.pack()
# call tick() function for clock label
tick()

root.mainloop()