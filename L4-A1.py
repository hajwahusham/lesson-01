from tkinter import *

window = Tk()
window.title('Tkinter sample window')
window.geometry("300x300")

#label
greetitg = Label(text="hello user", fg='black', bg='white')
#button
button = Button(text="click me", bg='black', fg='white')
#entry
entry = Entry(fg="yellow", bg="blue", width=100)

greetitg.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='sample frame')
label.pack()

textbox = Text(fg='green', bg='white')
textbox.pack()

window.mainloop()