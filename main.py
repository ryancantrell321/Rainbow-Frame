import tkinter as tk

window = tk.Tk()
window.title("Rainbow Frame")

frame1 = tk.Frame(master=window, width=200, height=150, bg="red")
frame2 = tk.Frame(master=window, width=200, height=150, bg="orange")
frame3 = tk.Frame(master=window, width=200, height=150, bg="yellow")
frame4 = tk.Frame(master=window, width=200, height=150, bg="green")
frame5 = tk.Frame(master=window, width=200, height=150, bg="cyan")
frame6 = tk.Frame(master=window, width=200, height=150, bg="blue")
frame7 = tk.Frame(master=window, width=200, height=150, bg="violet")

frames = frame1, frame2, frame3, frame4, frame5, frame6, frame7

for frameY in frames:
    frameY.pack(fill=tk.Y, side=tk.LEFT)


window.mainloop()

