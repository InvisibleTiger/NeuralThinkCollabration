import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Click the button below",
    fg="white",
    bg="black",
    width=25,
    height=5
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="yellow",
    fg="black"
)
button.pack()

entry = tk.Entry(
    fg="yellow",
    bg="white",
    width=25
)
entry.pack()

window.mainloop()