from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# setting up  main window
root = Tk()
root.title('denomination counter')
root.configure(bg='light sea green')
root.geometry('650x400')

# adding image and labels
upload = Image.open("img.jpg")
# resize the image
upload = upload.resize((300,300))
#convert image to tkinter compatible image
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root,
               text=" hello user!! welcome to denomination counter application",
               bg='light sea green')
label1.place(x=180, y=340)

# function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "alert!", "do you want to calculate the denomination count???")
    if MsgBox == 'ok':
        topwin()

    #adding buttons to the main window
button1 = Button(
    root,
    text="let's get started",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260, y=360)

#function for opening new/top window
def topwin():
    top = Toplevel()
    top.title('denominations calculator')
    top.configure(bg='light sea green')
    top.geometry('600x350')

    label = Label(top, text="enter total amount", bg='light grey')
    entry = Entry(top)
    lb1 = Label(top, text="here are number of notes forr each denommination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("error", "please enter a valid number")
    
    btn = Button(top, text='calculate', command=calculator, bg='brown', fg='white')

    # centering widgets in the top window
    label.place(x=200, y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lb1.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)

    top.mainloop()

root.mainloop()

