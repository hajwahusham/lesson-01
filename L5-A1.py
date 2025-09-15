# import all necessary libraries
# PIL (python imaging library) provides image editing capabilities to the python interpreter
from tkinter import *
from PIL import Image, ImageTk

# create a window
root = Tk()
root.title('image')
root.geometry('500x500')

# use Image.open to open and identify the given imagge file
upload = Image.open("img.jpg")

# convert the image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# add image to Tkinter label
label = Label(root, image=image, height=450, width=400)
label.place(x=50, y=0)
label2 = Label(root, text="this is how you add an image in Tkinter window")
label2.place(x=50, y=420)

# run the application
root.mainloop()