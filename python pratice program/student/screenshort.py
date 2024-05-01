from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
from ttkthemes import ThemedTk
import pyautogui
import time
root=ThemeTk(theme="radiance")
# root=tk()
root.title("Screenshot App")
root.geometry("500x400")

def screen():
    # hide the root window
    root.withdraw()


    time.sleep(3)

sc=pyautogui.screenshort()
save=messagebox.askyesno("Screenshot App","Do you want to save capture this picture?" )

if save:
    file=asksaveasfilename(defaultextension="png",
                           filetypes=[("All Files","*.*"),
                                      ("PNG file","*.png"),
                                      ("jpg file","*.jpg")])

    if file:
        sc.save(file)
        print("Screenshot Save...")

        root.deicoify()

        capture=ttk.Button(root,text="Take Screenshot",command=screen)
        capture.pack(pady=22)
        root.mainloop()