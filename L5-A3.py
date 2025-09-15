from tkinter import *

# settingup main window
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("150x150")
    top.title("toplevel")

    l2 = Label(top, text="this is a toplevel window")
    l2.pack()

    top.mainloop()

l = Label(root, text="this is the root window")
btn = Button(root, text= "click here to open another window", command= topwin)

l.pack()
btn.pack()

root.mainloop()