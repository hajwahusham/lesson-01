from tkinter import *
from tkinter import messagebox

# setup tkinter window
root = Tk()
root.geometry("200x200")

# function for displaying warning message
# messagebox.showwarning("windowname", "text to be displayed")
def msg():
    messagebox.showwarning("alert", "stop!!! virus found")

#adding button widget to window
button = Button(root, text="scan for viruses", command=msg)
button.place(x=50,y=80)

root.mainloop()