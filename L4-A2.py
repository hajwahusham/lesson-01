import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=5
        )
        frame.grid(row=i, column=j, padx=1, pady=1)
        label = tk.Label(master=frame, text=f"row {i}\ncloumn {j}")
        label.pack()

window.mainloop()